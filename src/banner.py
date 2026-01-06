# src/banner.py

"""
Beautiful CLI Banner for PAPER-CODE.
Uses Rich and Pyfiglet for stunning terminal output.
"""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.style import Style
from rich import box
import pyfiglet

# Version info
VERSION = "0.4.0"
AUTHOR = "PAPER-CODE Team"

# Initialize Rich console
console = Console()


def get_gradient_text(text: str, colors: list) -> Text:
    """
    Creates a gradient effect on text by applying different colors to each character.
    """
    rich_text = Text()
    color_count = len(colors)
    
    for i, char in enumerate(text):
        color_index = int((i / len(text)) * color_count)
        if color_index >= color_count:
            color_index = color_count - 1
        rich_text.append(char, style=Style(color=colors[color_index], bold=True))
    
    return rich_text


def display_banner():
    """
    Displays the beautiful PAPER-CODE banner with ASCII art and styling.
    """
    # Generate ASCII art using pyfiglet
    ascii_art = pyfiglet.figlet_format("PAPER-CODE", font="slant")
    
    # Define gradient colors (cyan to magenta spectrum)
    gradient_colors = [
        "#00d4ff",  # Bright cyan
        "#00b4ff",  # Light blue
        "#0094ff",  # Blue
        "#5f5fff",  # Purple-blue
        "#875fff",  # Purple
        "#af5fff",  # Magenta-purple
        "#d75fff",  # Magenta
    ]
    
    # Apply gradient to ASCII art
    gradient_ascii = get_gradient_text(ascii_art, gradient_colors)
    
    # Create subtitle with styling
    subtitle = Text()
    subtitle.append("📄 ", style="bold")
    subtitle.append("P", style="bold #00d4ff")
    subtitle.append("roject ", style="#888888")
    subtitle.append("A", style="bold #5f5fff")
    subtitle.append("rchitecture ", style="#888888")
    subtitle.append("P", style="bold #875fff")
    subtitle.append("atterns ", style="#888888")
    subtitle.append("E", style="bold #af5fff")
    subtitle.append("ngineering ", style="#888888")
    subtitle.append("R", style="bold #d75fff")
    subtitle.append("eferences", style="#888888")
    
    # Create description
    description = Text()
    description.append("\n✨ ", style="bold yellow")
    description.append("AI-Powered Documentation Generator for Modern Projects", style="italic #aaaaaa")
    description.append("\n\n")
    description.append("🚀 ", style="bold")
    description.append("Generate intelligent docs that work with ", style="#888888")
    description.append("Cursor", style="bold #00ff88")
    description.append(", ", style="#888888")
    description.append("Windsurf", style="bold #00d4ff")
    description.append(" & ", style="#888888")
    description.append("Copilot", style="bold #ff6b6b")
    
    # Combine all elements
    banner_content = Text()
    banner_content.append(gradient_ascii)
    banner_content.append("\n")
    banner_content.append(subtitle)
    banner_content.append(description)
    
    # Create the panel with fancy border
    panel = Panel(
        banner_content,
        box=box.DOUBLE_EDGE,
        border_style="bright_cyan",
        padding=(1, 4),
        title=f"[bold white]v{VERSION}[/]",
        title_align="right",
        subtitle="[dim]github.com/minhgiau998/paper-code[/]",
        subtitle_align="center",
    )
    
    console.print()
    console.print(panel)
    console.print()


def display_success_banner(output_path: str):
    """
    Displays a success banner after generation is complete.
    """
    success_text = Text()
    success_text.append("✨ ", style="bold yellow")
    success_text.append("Documentation Generated Successfully!", style="bold green")
    success_text.append("\n\n")
    success_text.append("📂 ", style="bold")
    success_text.append("Output: ", style="#888888")
    success_text.append(output_path, style="bold cyan underline")
    success_text.append("\n\n")
    success_text.append("🤖 ", style="bold")
    success_text.append("Next Steps:", style="bold white")
    success_text.append("\n   → Open this folder in ", style="#888888")
    success_text.append("Cursor", style="bold #00ff88")
    success_text.append(" or ", style="#888888")
    success_text.append("Windsurf", style="bold #00d4ff")
    success_text.append("\n   → AI will automatically use your new documentation!", style="#888888")
    
    panel = Panel(
        success_text,
        box=box.ROUNDED,
        border_style="green",
        padding=(1, 3),
    )
    
    console.print()
    console.print(panel)


def display_divider(title: str = ""):
    """
    Displays a styled divider with optional title.
    """
    if title:
        console.rule(f"[bold cyan]{title}[/]", style="dim")
    else:
        console.rule(style="dim")


if __name__ == "__main__":
    # Test the banner
    display_banner()
    display_divider("Configuration")
    console.print("\n[dim]This is where prompts would appear...[/]\n")
    display_success_banner("D:/Projects/my-project/output")
