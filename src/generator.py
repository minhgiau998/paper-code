# src/generator.py

import os
import logging
from typing import Dict, Any, List
from jinja2 import Environment, FileSystemLoader, TemplateNotFound

# Configure logging for clearer output
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("PaperCLI")

class DocGenerator:
    """
    Handles the generation of documentation files using Jinja2 templates.
    It maps the user's selection (Stack, Libraries) to specific template files
    and renders them into the output directory.
    """

    def __init__(self, output_dir: str):
        """
        Initialize the generator with the output directory.
        
        Args:
            output_dir (str): The root path where files will be generated.
        """
        self.output_dir = output_dir
        
        # Determine the absolute path to the 'templates' directory
        # This assumes the structure: src/generator.py -> src/templates/
        base_dir = os.path.dirname(os.path.abspath(__file__))
        template_dir = os.path.join(base_dir, "templates")
        
        # Initialize Jinja2 Environment
        # trim_blocks=True and lstrip_blocks=True help keep the Markdown output clean
        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True
        )

    def _sanitize_name(self, name: str) -> str:
        """
        Helper to convert display names into filesystem-friendly names.
        Example: "Node.js (Commander)" -> "nodejs_commander"
        """
        return (
            name.lower()
            .replace(" ", "_")
            .replace(".", "")
            .replace("(", "")
            .replace(")", "")
            .replace("/", "_")
            .replace("-", "_")
        )

    def _render(self, template_path: str, context: Dict[str, Any], output_rel_path: str):
        """
        Internal method to render a single template to a file.
        
        Args:
            template_path (str): Path to the template relative to the 'templates' folder.
            context (Dict): Dictionary containing data for Jinja2 (project_name, stack, etc.).
            output_rel_path (str): Desired output path relative to the project root.
        """
        try:
            template = self.env.get_template(template_path)
            content = template.render(context)

            # Construct full output path
            full_path = os.path.join(self.output_dir, output_rel_path)
            
            # Ensure the directory exists
            os.makedirs(os.path.dirname(full_path), exist_ok=True)

            # Write the file
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)
            
            logger.info(f"✅ Generated: {output_rel_path}")

        except TemplateNotFound:
            logger.warning(f"⚠️ Template not found: {template_path}. Skipping {output_rel_path}.")
        except Exception as e:
            logger.error(f"❌ Error generating {output_rel_path}: {str(e)}")

    def generate_project(self, context: Dict[str, Any]):
        """
        Main entry point to generate the full project documentation structure.
        
        Structure generated (based on README.md):
        - Root: README.md, CHANGELOG.md, LICENSE
        - docs/ai/: AI_RULES.md, AI_WORKFLOWS.md, AI_CONTEXT.md
        - docs/: ARCHITECTURE.md, CODE_STANDARDS.md, CONTRIBUTING.md, DEPLOYMENT.md, SECURITY.md
        - docs/libs/: (Optional) Library specific docs
        """
        logger.info(f"🚀 Starting generation for stack: {context['tech_stack']}")

        # Prepare sanitized names for template lookups
        stack_safe = self._sanitize_name(context["tech_stack"])
        type_safe = self._sanitize_name(context["project_type"])

        # ---------------------------------------------------------
        # 1. Root Level Files
        # ---------------------------------------------------------
        self._render("core/README.md.j2", context, "README.md")
        self._render("core/LICENSE.j2", context, "LICENSE")
        self._render("core/CHANGELOG.md.j2", context, "CHANGELOG.md")
        self._render("core/gitignore.j2", context, ".gitignore")

        # ---------------------------------------------------------
        # 2. AI Documentation (The Core Value Prop)
        # ---------------------------------------------------------
        # These files provide context to Cursor/Copilot
        self._render("ai/AI_RULES.md.j2", context, "docs/ai/AI_RULES.md")
        self._render("ai/AI_WORKFLOWS.md.j2", context, "docs/ai/AI_WORKFLOWS.md")
        self._render("ai/AI_CONTEXT.md.j2", context, "docs/ai/AI_CONTEXT.md")
        
        # Editor specific rules (e.g. .cursorrules)
        self._render("ai/cursorrules.j2", context, ".cursorrules")

        # Copilot Instructions (.github)
        self._render("ai/copilot-instructions.md.j2", context, ".github/copilot-instructions.md")

        # ---------------------------------------------------------
        # 3. Governance & Standards (docs folder)
        # ---------------------------------------------------------
        self._render("core/CONTRIBUTING.md.j2", context, "docs/CONTRIBUTING.md")
        self._render("core/SECURITY.md.j2", context, "docs/SECURITY.md")
        self._render("core/TESTING.md.j2", context, "docs/TESTING.md")
        self._render("core/DEPLOYMENT.md.j2", context, "docs/DEPLOYMENT.md")

        # ---------------------------------------------------------
        # 4. Tech Stack Specific Files
        # ---------------------------------------------------------
        # We try to find specific templates for the stack (e.g., stacks/frontend/react.md.j2).
        # If not found, we fall back to a generic one or skip.
        
        # ARCHITECTURE.md: Usually highly specific to the stack
        arch_template = f"stacks/{type_safe}/{stack_safe}_arch.md.j2"
        self._render(arch_template, context, "docs/ARCHITECTURE.md")

        # CODE_STANDARDS.md: Specific to the stack
        standards_template = f"stacks/{type_safe}/{stack_safe}_standards.md.j2"
        self._render(standards_template, context, "docs/CODE_STANDARDS.md")

        # ---------------------------------------------------------
        # 5. Library / Module Documentation
        # ---------------------------------------------------------
        # If the user selected libraries (e.g., Axios, Tailwind), generate docs for them.
        libraries = context.get("libraries", [])
        if libraries:
            logger.info(f"📚 Generating docs for libraries: {', '.join(libraries)}")
            
            for lib in libraries:
                lib_safe = self._sanitize_name(lib)
                
                # Check for specific library template
                lib_template = f"libs/{lib_safe}.md.j2"
                
                # We render these into a 'libs' subfolder to keep 'docs' clean
                # but they are referenced in AI_CONTEXT.md
                self._render(lib_template, context, f"docs/libs/{lib_safe}.md")

        logger.info("\n✨ Project documentation generated successfully!")

        # ---------------------------------------------------------
        # 6. Github folder (.github)
        # ---------------------------------------------------------
        # Tạo thư mục .github
        os.makedirs(os.path.join(self.output_dir, ".github/workflows"), exist_ok=True)

        # Render CI Workflow
        self._render("github/ci.yml.j2", context, ".github/workflows/ci.yml")

        # Render PR Template
        self._render("github/PULL_REQUEST_TEMPLATE.md.j2", context, ".github/PULL_REQUEST_TEMPLATE.md")

        # Render Copilot Instructions (Nếu chưa render ở bước AI)
        self._render("ai/copilot-instructions.md.j2", context, ".github/copilot-instructions.md")

        logger.info("✅ Generated .github configurations")