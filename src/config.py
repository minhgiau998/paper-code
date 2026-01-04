# src/config.py

"""
Configuration file for PAPER-CODE.
This file defines the available project types, technology stacks, and optional libraries/modules.
It acts as the single source of truth for the CLI selection menus.
"""

from typing import Dict, List

# =============================================================================
# 1. Project Types
# =============================================================================
# These correspond to the top-level categories in the CLI interactive mode.
PROJECT_TYPES: List[str] = [
    "Frontend",
    "Backend",
    "Mobile",
    "Desktop",
    "Data & ML",
    "Game",
    "CLI",
    "Library",
]

# =============================================================================
# 2. Technology Stacks
# =============================================================================
# Mapping between Project Type and specific Tech Stacks.
# Keys must match the items in PROJECT_TYPES.
TECH_STACKS: Dict[str, List[str]] = {
    "Frontend": [
        "React",
        "Vue",
        "Next.js",
        "Nuxt.js",
        "Angular",
        "Svelte",
    ],
    "Backend": [
        "Node.js",
        "FastAPI",
        "Django",
        "Go (Gin)",
    ],
    "Mobile": [
        "React Native",
        "Flutter",
    ],
    "Desktop": [
        "Electron",
        "Tauri",
    ],
    "Data & ML": [
        "PyTorch",
        "TensorFlow",
        "Scikit-learn",
    ],
    "Game": [
        "Godot",
        "Unity",
    ],
    "CLI": [
        "Node.js (Commander)",
        "Python (Click)",
        "Go (Cobra)",
        "Rust (Clap)",
    ],
    "Library": [
        "TypeScript Lib",
        "Python Lib",
        "Go Lib",
        "Rust Lib",
    ],
}

# =============================================================================
# 3. Libraries & Modules
# =============================================================================
# Optional modules that users can select for specific stacks.
# Keys should match the items in the TECH_STACKS lists.
#
# NOTE: Common libraries can be repeated across compatible stacks.
LIBRARIES: Dict[str, List[str]] = {
    # --- Frontend Stacks ---
    "React": [
        "Axios", "TanStack Query", "TailwindCSS", "Redux Toolkit", "Zustand", 
        "React Router", "Zod", "Jest", "Vite"
    ],
    "Vue": [
        "Axios", "Pinia", "Vue Router", "TailwindCSS", "Vitest"
    ],
    "Next.js": [
        "Axios", "TailwindCSS", "Prisma", "NextAuth.js", "Zod", "Shadcn UI"
    ],
    "Nuxt.js": [
        "TailwindCSS", "Pinia", "Nuxt UI", "Supabase", "Prisma", "Zod", "i18n"
    ],
    "Angular": [
        "RxJS", "NgRx", "Angular Material", "TailwindCSS"
    ],
    "Svelte": [
        "Axios", "TailwindCSS", "SvelteKit"
    ],

    # --- Backend Stacks ---
    "Node.js": [
        "Express", "NestJS", "Fastify", "Mongoose", "TypeORM", "Prisma", 
        "Socket.io", "Winston", "Jest"
    ],
    "FastAPI": [
        "SQLAlchemy", "Pydantic", "Alembic", "Tortoise-ORM", "Redis", "Celery", "Pytest"
    ],
    "Django": [
        "Django REST Framework", "Celery", "Redis", "PostgreSQL", "Gunicorn"
    ],
    "Go (Gin)": [
        "Gorm", "Viper", "Zap", "Redis", "PostgreSQL Driver"
    ],

    # --- Mobile Stacks ---
    "React Native": [
        "React Navigation", "Expo", "Reanimated", "Axios", "Redux Toolkit"
    ],
    "Flutter": [
        "Bloc", "Riverpod", "Provider", "Dio", "GetX", "Hive"
    ],

    # --- Desktop Stacks ---
    "Electron": [
        "React", "Vue", "Electron Builder", "TailwindCSS"
    ],
    "Tauri": [
        "React", "Svelte", "Rust", "TailwindCSS"
    ],

    # --- Data & ML Stacks ---
    "PyTorch": [
        "Pandas", "NumPy", "Matplotlib", "Torchaudio", "Torchvision", "Jupyter"
    ],
    "TensorFlow": [
        "Pandas", "NumPy", "Matplotlib", "Keras", "Jupyter"
    ],
    "Scikit-learn": [
        "Pandas", "NumPy", "Matplotlib", "Seaborn", "Jupyter"
    ],

    # --- Game Stacks ---
    "Godot": [
        "GDScript", "C#", "Godot Steam"
    ],
    "Unity": [
        "C#", "Addressables", "Cinemachine", "Input System", "XR Interaction Toolkit"
    ],

    # --- CLI Stacks ---
    "Node.js (Commander)": [
        "Inquirer", "Chalk", "Ora", "Figlet"
    ],
    "Python (Click)": [
        "Rich", "Typer", "Colorama", "Tqdm"
    ],
    "Go (Cobra)": [
        "Viper", "Pflag", "Bubbletea"
    ],
    "Rust (Clap)": [
        "Serde", "Tokio", "Anyhow", "Indicatif"
    ],

    # --- Library Stacks ---
    "TypeScript Lib": [
        "Jest", "Vitest", "ESLint", "Prettier", "Rollup"
    ],
    "Python Lib": [
        "Pytest", "Setuptools", "Poetry", "Black", "Mypy"
    ],
    "Go Lib": [
        "Testify", "GoDoc"
    ],
    "Rust Lib": [
        "Cargo", "Criterion"
    ],
}

# =============================================================================
# 4. Helper Mappings (Optional)
# =============================================================================
# Defines the standard file extension or primary language for the stack.
# Useful for file generation logic (e.g., creating .py vs .ts files).
STACK_EXTENSIONS: Dict[str, str] = {
    "React": "jsx",
    "Vue": "vue",
    "Next.js": "tsx",
    "Node.js": "js",
    "FastAPI": "py",
    "Django": "py",
    "Go (Gin)": "go",
    "Rust (Clap)": "rs",
    "Python (Click)": "py",
}