# src/main.py

import typer
import inquirer
import json
import os
import sys
from typing import Optional, List, Dict, Any
from pathlib import Path

# Internal modules
from src.config import PROJECT_TYPES, TECH_STACKS, LIBRARIES
from src.generator import DocGenerator
from src.banner import display_banner, display_success_banner, display_divider

# Initialize Typer app
app = typer.Typer(
    help="PAPER-CODE: Interactive Project Documentation Generator",
    add_completion=False
)

def load_config_file(config_path: str) -> Dict[str, Any]:
    """
    Loads project configuration from a JSON file.
    Useful for batch mode or re-running previous setups.
    """
    if not os.path.exists(config_path):
        typer.secho(f"❌ Config file not found: {config_path}", fg=typer.colors.RED)
        sys.exit(1)
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        typer.secho(f"❌ Invalid JSON in config file: {config_path}", fg=typer.colors.RED)
        sys.exit(1)

def save_config_file(data: Dict[str, Any], output_path: str = "paper-config.json"):
    """
    Saves the current configuration to a JSON file.
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
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
        help="Load project configuration from a JSON file."
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
    # 2. Batch Mode Validation
    # ---------------------------------------------------------
    if batch:
        if not context:
            typer.secho("❌ Batch mode requires a valid config file via --config.", fg=typer.colors.RED)
            raise typer.Exit(code=1)
        
        # In batch mode, we skip prompts and jump straight to generation
        typer.secho("🚀 Running in Batch Mode...", fg=typer.colors.BLUE)
        run_generator(output, context)
        return

    # ---------------------------------------------------------
    # 3. Interactive Mode (Inquirer)
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
    # Use CLI arg --template or config if available, else prompt
    selected_type = template or context.get("project_type")
    
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
        q_type = [
            inquirer.List(
                "project_type", 
                message="Select Project Type", 
                choices=PROJECT_TYPES
            )
        ]
        ans_type = inquirer.prompt(q_type)
        if not ans_type: raise typer.Exit()
        selected_type = ans_type["project_type"]
    
    context["project_type"] = selected_type

    # -- Question: Tech Stack --
    # Dependent on Project Type
    selected_stack = context.get("tech_stack")
    available_stacks = TECH_STACKS.get(selected_type, [])

    if not selected_stack:
        if not available_stacks:
            typer.secho(f"⚠️ No defined stacks for {selected_type}. Skipping stack selection.", fg=typer.colors.YELLOW)
            context["tech_stack"] = "Generic"
        else:
            q_stack = [
                inquirer.List(
                    "tech_stack", 
                    message=f"Select {selected_type} Stack", 
                    choices=available_stacks
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
            q_libs = [
                inquirer.Checkbox(
                    "libraries", 
                    message="Select Modules/Libraries (Space to select, Enter to confirm)", 
                    choices=available_libs
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