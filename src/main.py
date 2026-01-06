# src/main.py

import typer
import inquirer
import json
import os
import sys
from typing import Optional, List, Dict, Any
from pathlib import Path

# Internal modules
from .config import PROJECT_TYPES, TECH_STACKS, LIBRARIES
from .generator import DocGenerator
from .banner import display_banner, display_success_banner, display_divider
from .detector import detect_project_context

# Initialize Typer app
app = typer.Typer(
    help="PAPER-CODE: Interactive Project Documentation Generator",
    add_completion=False
)

def load_config_file(config_path: str) -> Dict[str, Any]:
    """
    Loads project configuration from a JSON file.
    Useful for batch mode or re-running previous setups.
    Supports both 'paper.config.json' and 'paper-config.json' for backward compatibility.
    """
    # Try paper.config.json first (new standard), then paper-config.json (legacy)
    if not os.path.exists(config_path):
        # Auto-detect common config file names
        if config_path == "paper.config.json" or config_path == "paper-config.json":
            alt_path = "paper-config.json" if config_path == "paper.config.json" else "paper.config.json"
            if os.path.exists(alt_path):
                config_path = alt_path
                typer.secho(f"ℹ️  Using config file: {config_path}", fg=typer.colors.BLUE)
            else:
                typer.secho(f"❌ Config file not found: {config_path}", fg=typer.colors.RED)
                sys.exit(1)
        else:
            typer.secho(f"❌ Config file not found: {config_path}", fg=typer.colors.RED)
            sys.exit(1)
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        typer.secho(f"❌ Invalid JSON in config file: {config_path}", fg=typer.colors.RED)
        typer.secho(f"   Error: {e}", fg=typer.colors.RED)
        sys.exit(1)

def save_config_file(data: Dict[str, Any], output_path: str = "paper.config.json"):
    """
    Saves the current configuration to a JSON file.
    Defaults to paper.config.json (new standard).
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        typer.secho(f"💾 Configuration saved to: {output_path}", fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho(f"⚠️ Failed to save config: {e}", fg=typer.colors.YELLOW)

@app.command()
def main(
    output: str = typer.Option(
        "./output/", 
        "--output", "-o", 
        help="Output directory for the generated project (default: ./output/)."
    ),
    config: Optional[str] = typer.Option(
        None, 
        "--config", "-c", 
        help="Load project configuration from a JSON file (paper.config.json or paper-config.json)."
    ),
    batch: bool = typer.Option(
        False, 
        "--batch", "-b", 
        help="Non-interactive batch mode (requires --config)."
    ),
    template: Optional[str] = typer.Option(
        None, 
        "--template", "-t", 
        help=f"Pre-select a project type (e.g., Frontend, Backend)."
    ),
    save_config: bool = typer.Option(
        False, 
        "--save-config", 
        help="Save the final configuration to a JSON file."
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        help="Enable verbose output."
    )
):
    """
    Main entry point for PAPER-CODE.
    Generates documentation structures based on user input or configuration files.
    """
    
    # Context dictionary that will hold all project data
    context: Dict[str, Any] = {}

    # ---------------------------------------------------------
    # 1. Load Configuration (Batch / Preset)
    # ---------------------------------------------------------
    if config:
        context = load_config_file(config)
        if verbose:
            typer.echo(f"Loaded config: {context}")

    # ---------------------------------------------------------
    # 2. Smart Detection (if no config provided)
    # ---------------------------------------------------------
    detected_suggestions = None
    if not context and not batch:
        # Avoid self-detection when developing PAPER-CODE itself.
        # Check pyproject.toml for the package name to skip detection inside this repo.
        try:
            cwd = Path(".").resolve()
            pyproject = cwd / "pyproject.toml"
            is_self_repo = False
            if pyproject.exists():
                try:
                    content = pyproject.read_text(encoding='utf-8')
                    if 'name = "paper-code"' in content or "name = 'paper-code'" in content:
                        is_self_repo = True
                except Exception:
                    is_self_repo = False
        except Exception:
            is_self_repo = False

        if not is_self_repo:
            # Only run detection in interactive mode when no config is provided
            detected_suggestions = detect_project_context(".")
            if detected_suggestions:
                typer.secho("🔍 Detected project files! Suggestions will be pre-filled.", fg=typer.colors.GREEN)
                if verbose:
                    typer.echo(f"Detection results: {detected_suggestions}")
        else:
            if verbose:
                typer.echo("ℹ️  Skipping autodetection because running inside PAPER-CODE repository.")

    # ---------------------------------------------------------
    # 3. Batch Mode Validation
    # ---------------------------------------------------------
    if batch:
        if not context:
            # Try to auto-detect config file
            for config_name in ["paper.config.json", "paper-config.json"]:
                if os.path.exists(config_name):
                    typer.secho(f"ℹ️  Auto-detected config file: {config_name}", fg=typer.colors.BLUE)
                    context = load_config_file(config_name)
                    break
            
            if not context:
                typer.secho("❌ Batch mode requires a valid config file via --config or paper.config.json in current directory.", fg=typer.colors.RED)
                raise typer.Exit(code=1)
        
        # In batch mode, we skip prompts and jump straight to generation
        typer.secho("🚀 Running in Batch Mode...", fg=typer.colors.BLUE)
        run_generator(output, context)
        return

    # ---------------------------------------------------------
    # 4. Interactive Mode (Inquirer)
    # ---------------------------------------------------------
    # Display beautiful banner
    display_banner()
    display_divider("Project Configuration")
    typer.echo()

    # Define prompts dynamically based on what's already in context (from config)
    questions = []

    # -- Question: Project Name --
    if "project_name" not in context:
        questions.append(
            inquirer.Text("project_name", message="Project Name", default="My Project")
        )

    # -- Question: Description (AI Context) --
    if "description" not in context:
        questions.append(
            inquirer.Text(
                "description", 
                message="Project Description (This helps AI understand your goal)", 
                default="A robust project using modern technologies."
            )
        )

    # Prompt generic info first
    if questions:
        answers = inquirer.prompt(questions)
        if not answers: raise typer.Exit() # Handle Ctrl+C
        context.update(answers)

    # -- Question: Project Type --
    # Use CLI arg --template, config, or detected suggestion
    selected_type = template or context.get("project_type") or (detected_suggestions.get("project_type") if detected_suggestions else None)
    
    # Validate template argument
    if selected_type and selected_type not in PROJECT_TYPES:
         # Try case-insensitive matching
         match = next((t for t in PROJECT_TYPES if t.lower() == selected_type.lower()), None)
         if match:
             selected_type = match
         else:
             typer.secho(f"⚠️ Template '{selected_type}' not found. Falling back to selection.", fg=typer.colors.YELLOW)
             selected_type = None

    if not selected_type:
        # Pre-select detected type if available
        default_choice = None
        choices = PROJECT_TYPES
        if detected_suggestions and detected_suggestions.get("project_type") in PROJECT_TYPES:
            default_choice = detected_suggestions["project_type"]
            # Move detected type to top of list
            choices = [default_choice] + [t for t in PROJECT_TYPES if t != default_choice]
        
        q_type = [
            inquirer.List(
                "project_type", 
                message="Select Project Type" + (f" (Detected: {default_choice})" if default_choice else ""), 
                choices=choices,
                default=default_choice
            )
        ]
        ans_type = inquirer.prompt(q_type)
        if not ans_type: raise typer.Exit()
        selected_type = ans_type["project_type"]
    
    context["project_type"] = selected_type

    # -- Question: Tech Stack --
    # Dependent on Project Type
    selected_stack = context.get("tech_stack") or (detected_suggestions.get("tech_stack") if detected_suggestions else None)
    available_stacks = TECH_STACKS.get(selected_type, [])

    if not selected_stack:
        if not available_stacks:
            typer.secho(f"⚠️ No defined stacks for {selected_type}. Skipping stack selection.", fg=typer.colors.YELLOW)
            context["tech_stack"] = "Generic"
        else:
            # Pre-select detected stack if available and valid
            default_stack = None
            if detected_suggestions and detected_suggestions.get("tech_stack") in available_stacks:
                default_stack = detected_suggestions["tech_stack"]
                # Move detected stack to top
                available_stacks = [default_stack] + [s for s in available_stacks if s != default_stack]
            
            q_stack = [
                inquirer.List(
                    "tech_stack", 
                    message=f"Select {selected_type} Stack" + (f" (Detected: {default_stack})" if default_stack else ""), 
                    choices=available_stacks,
                    default=default_stack
                )
            ]
            ans_stack = inquirer.prompt(q_stack)
            if not ans_stack: raise typer.Exit()
            selected_stack = ans_stack["tech_stack"]
            context["tech_stack"] = selected_stack

    # -- Question: Libraries / Modules --
    # Dependent on Tech Stack
    # If config already has libraries, we respect it. Otherwise, we ask.
    if "libraries" not in context:
        available_libs = LIBRARIES.get(selected_stack, [])
        if available_libs:
            # Pre-select detected libraries if available
            default_libs = []
            if detected_suggestions and detected_suggestions.get("libraries"):
                # Only include detected libraries that are actually available for this stack
                default_libs = [lib for lib in detected_suggestions["libraries"] if lib in available_libs]
            
            q_libs = [
                inquirer.Checkbox(
                    "libraries", 
                    message="Select Modules/Libraries (Space to select, Enter to confirm)" + (f" (Detected: {len(default_libs)} libs)" if default_libs else ""), 
                    choices=available_libs,
                    default=default_libs
                )
            ]
            ans_libs = inquirer.prompt(q_libs)
            if not ans_libs: raise typer.Exit()
            context["libraries"] = ans_libs["libraries"]
        else:
            context["libraries"] = []

    # ---------------------------------------------------------
    # 4. Final Execution
    # ---------------------------------------------------------
    if verbose:
        typer.echo(f"\n📋 Final Configuration:\n{json.dumps(context, indent=2)}\n")

    # Save config if requested
    if save_config:
        save_config_file(context)

    run_generator(output, context)


def run_generator(output_dir: str, context: Dict[str, Any]):
    """
    Instantiates the generator and runs the rendering process.
    """
    try:
        gen = DocGenerator(output_dir)
        gen.generate_project(context)
        
        # Success message with beautiful banner
        display_success_banner(os.path.abspath(output_dir))
        
    except Exception as e:
        typer.secho(f"❌ Error during generation: {e}", fg=typer.colors.RED)
        sys.exit(1)


if __name__ == "__main__":
    app()