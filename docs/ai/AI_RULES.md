# AI Rules for PAPER-CODE Development

## 🧠 Project Context
This is a **Python CLI Tool** built with **Typer** and **Jinja2**.
It generates markdown documentation for other developers.

## 🛡️ Coding Standards

### 1. Python Style
- Use **Type Hints** strictly (`def func(name: str) -> bool:`).
- Use `pathlib` or `os.path` for cross-platform compatibility.
- **Sanitization:** Always sanitize user input before using it to find file paths. Use the `_sanitize_name` helper in `generator.py`.

### 2. Jinja2 Templates
- **Extension:** All templates must end in `.md.j2` or `.j2`.
- **Logic:** Keep Jinja logic simple (`{% if %}`, `{% for %}`). Avoid complex processing inside templates; move that to Python.
- **Context Awareness:** Always assume variables like `tech_stack` and `libraries` might be missing or empty. Use `| default` filters if necessary.

### 3. Config Management
- **Single Source of Truth:** `src/config.py` defines what is possible. Do not hardcode stack names in `main.py` or `generator.py`.

## 🧪 Testing Strategy
- To test a new template, run the CLI in dry-run or debug mode.
- Use `pytest` for unit testing the logic in `generator.py`.