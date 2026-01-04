# Architecture of PAPER-CODE

## 🏗️ Design Philosophy

**PAPER-CODE** follows a **Data-Driven Architecture**. The logic is separated into:
1.  **Configuration (`src/config.py`):** The single source of truth for supported Stacks and Libraries.
2.  **Templates (`src/templates/`):** Logic-less Jinja2 templates.
3.  **Generator (`src/generator.py`):** The engine that marries Config with Templates.
4.  **CLI (`src/main.py`):** The user interface layer using Typer/Inquirer.

## 🔄 Execution Flow

1.  **User Input:** User runs `paper-code init` or passes flags.
2.  **Context Building:** `main.py` builds a `context` dictionary:
    ```python
    context = {
        "project_name": "My App",
        "tech_stack": "React",
        "libraries": ["TailwindCSS", "Axios"]
    }
    ```
3.  **Sanitization:** `generator.py` converts "React Native" -> `react_native`.
4.  **Template Resolution:**
    - The generator looks for specific templates: `src/templates/stacks/mobile/react_native_arch.md.j2`.
    - If found, it renders using the context.
    - If not found, it skips or uses a fallback.
5.  **Output:** Files are written to the target directory.

## 📂 Directory Structure

```text
src/
├── config.py            # 1. CONSTANTS (Project Types, Stacks, Libs)
├── generator.py         # 2. Logic (Jinja2 Env, Render methods)
├── main.py              # 3. Entry Point (Typer CLI)
└── templates/           # 4. The Content
    ├── core/            # README, LICENSE, GITIGNORE
    ├── ai/              # AI Rules & Context
    ├── stacks/          # Stack-specific docs (Arch, Standards)
    │   ├── frontend/
    │   ├── backend/
    │   └── ...
    └── libs/            # Library-specific snippets
```