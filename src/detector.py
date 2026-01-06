# src/detector.py

"""
Smart Detection Module for PAPER-CODE.
Automatically detects project type and tech stack from existing project files.
"""

import os
import json
from typing import Dict, List, Optional, Tuple
from pathlib import Path

# Mapping from detected files to suggested stacks
DETECTION_MAPPINGS = {
    # Node.js / Frontend
    "package.json": {
        "project_type": "Frontend",
        "tech_stack_candidates": ["React", "Vue", "Next.js", "Nuxt.js", "Angular", "Svelte"],
        "library_hints": {
            "react": "React",
            "vue": "Vue",
            "next": "Next.js",
            "nuxt": "Nuxt.js",
            "@angular/core": "Angular",
            "svelte": "Svelte",
        }
    },
    # Python Backend
    "requirements.txt": {
        "project_type": "Backend",
        "tech_stack_candidates": ["FastAPI", "Django"],
        "library_hints": {
            "fastapi": "FastAPI",
            "django": "Django",
            "flask": None,  # Not yet supported
        }
    },
    "pyproject.toml": {
        "project_type": "Backend",
        "tech_stack_candidates": ["FastAPI", "Django"],
        "library_hints": {
            "fastapi": "FastAPI",
            "django": "Django",
        }
    },
    "setup.py": {
        "project_type": "Backend",
        "tech_stack_candidates": ["FastAPI", "Django"],
        "library_hints": {}
    },
    # Go
    "go.mod": {
        "project_type": "Backend",
        "tech_stack_candidates": ["Go (Gin)"],
        "library_hints": {
            "github.com/gin-gonic/gin": "Go (Gin)",
        }
    },
    # Rust
    "Cargo.toml": {
        "project_type": "CLI",
        "tech_stack_candidates": ["Rust (Clap)"],
        "library_hints": {
            "clap": "Rust (Clap)",
        }
    },
    # Mobile
    "pubspec.yaml": {
        "project_type": "Mobile",
        "tech_stack_candidates": ["Flutter"],
        "library_hints": {}
    },
    "android/app/build.gradle": {
        "project_type": "Mobile",
        "tech_stack_candidates": ["Kotlin (Android)"],
        "library_hints": {}
    },
    "ios/Podfile": {
        "project_type": "Mobile",
        "tech_stack_candidates": ["Swift (iOS)"],
        "library_hints": {}
    },
    # React Native
    "app.json": {
        "project_type": "Mobile",
        "tech_stack_candidates": ["React Native"],
        "library_hints": {}
    },
    # Desktop
    "electron-builder.yml": {
        "project_type": "Desktop",
        "tech_stack_candidates": ["Electron"],
        "library_hints": {}
    },
    "tauri.conf.json": {
        "project_type": "Desktop",
        "tech_stack_candidates": ["Tauri"],
        "library_hints": {}
    },
    # DevOps
    "Dockerfile": {
        "project_type": "DevOps",
        "tech_stack_candidates": ["Docker"],
        "library_hints": {}
    },
    "docker-compose.yml": {
        "project_type": "DevOps",
        "tech_stack_candidates": ["Docker"],
        "library_hints": {}
    },
    "k8s": {  # Directory check
        "project_type": "DevOps",
        "tech_stack_candidates": ["Kubernetes"],
        "library_hints": {}
    },
    "*.tf": {  # Terraform files
        "project_type": "DevOps",
        "tech_stack_candidates": ["Terraform"],
        "library_hints": {}
    },
}


def detect_project_files(base_path: str = ".") -> List[Tuple[str, str]]:
    """
    Scans the current directory for project configuration files.
    
    Returns:
        List of tuples: (file_path, detection_key)
    """
    base = Path(base_path).resolve()
    detected = []
    
    for detection_key, config in DETECTION_MAPPINGS.items():
        # Handle special cases
        if detection_key == "k8s":
            # Check for k8s directory
            k8s_dir = base / "k8s"
            if k8s_dir.exists() and k8s_dir.is_dir():
                detected.append((str(k8s_dir), detection_key))
        elif detection_key == "*.tf":
            # Check for .tf files
            for tf_file in base.rglob("*.tf"):
                if tf_file.is_file():
                    detected.append((str(tf_file), detection_key))
                    break  # One is enough
        elif detection_key == "android/app/build.gradle":
            # Check nested path
            gradle_file = base / "android" / "app" / "build.gradle"
            if gradle_file.exists():
                detected.append((str(gradle_file), detection_key))
        elif detection_key == "ios/Podfile":
            # Check nested path
            podfile = base / "ios" / "Podfile"
            if podfile.exists():
                detected.append((str(podfile), detection_key))
        else:
            # Simple file check
            file_path = base / detection_key
            if file_path.exists() and file_path.is_file():
                detected.append((str(file_path), detection_key))
    
    return detected


def analyze_package_json(package_json_path: str) -> Dict[str, any]:
    """
    Analyzes package.json to extract dependencies and suggest tech stack.
    
    Returns:
        Dict with suggested tech_stack and libraries
    """
    suggestions = {
        "tech_stack": None,
        "libraries": []
    }
    
    try:
        with open(package_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        dependencies = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
        dep_names_lower = {k.lower(): k for k in dependencies.keys()}
        
        # Check for tech stack
        detection_config = DETECTION_MAPPINGS["package.json"]
        for dep_key, suggested_stack in detection_config["library_hints"].items():
            if dep_key in dep_names_lower:
                suggestions["tech_stack"] = suggested_stack
                break
        
        # Check for common libraries
        from src.config import LIBRARIES
        
        # Common library mappings (case-insensitive)
        library_mappings = {
            "axios": "Axios",
            "react-router": "React Router",
            "react-router-dom": "React Router",
            "@tanstack/react-query": "TanStack Query",
            "@reduxjs/toolkit": "Redux Toolkit",
            "zustand": "Zustand",
            "tailwindcss": "TailwindCSS",
            "zod": "Zod",
            "jest": "Jest",
            "vitest": "Vitest",
            "vite": "Vite",
            "pinia": "Pinia",
            "vue-router": "Vue Router",
            "@prisma/client": "Prisma",
            "next-auth": "NextAuth.js",
            "@next-auth/prisma-adapter": "NextAuth.js",
            "next-intl": "i18n",
            "vue-i18n": "i18n",
            "react-i18next": "i18n",
            "@supabase/supabase-js": "Supabase",
            "rxjs": "RxJS",
            "@ngrx/store": "NgRx",
            "@angular/material": "Angular Material",
            "express": "Express",
            "@nestjs/core": "NestJS",
            "fastify": "Fastify",
            "mongoose": "Mongoose",
            "typeorm": "TypeORM",
            "socket.io": "Socket.io",
            "winston": "Winston",
        }
        
        for dep_lower, lib_name in library_mappings.items():
            if dep_lower in dep_names_lower:
                suggestions["libraries"].append(lib_name)
        
        # Remove duplicates
        suggestions["libraries"] = list(set(suggestions["libraries"]))
        
    except (json.JSONDecodeError, FileNotFoundError, KeyError) as e:
        pass  # Silently fail, return empty suggestions
    
    return suggestions


def analyze_requirements_txt(requirements_path: str) -> Dict[str, any]:
    """
    Analyzes requirements.txt to suggest Python backend stack and libraries.
    
    Returns:
        Dict with suggested tech_stack and libraries
    """
    suggestions = {
        "tech_stack": None,
        "libraries": []
    }
    
    try:
        with open(requirements_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Normalize package names (remove version specifiers)
        packages = []
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                # Extract package name (before ==, >=, etc.)
                pkg_name = line.split('==')[0].split('>=')[0].split('<=')[0].split('>')[0].split('<')[0].strip().lower()
                packages.append(pkg_name)
        
        # Check for tech stack
        if "fastapi" in packages:
            suggestions["tech_stack"] = "FastAPI"
        elif "django" in packages:
            suggestions["tech_stack"] = "Django"
        
        # Check for common libraries
        library_mappings = {
            "sqlalchemy": "SQLAlchemy",
            "pydantic": "Pydantic",
            "alembic": "Alembic",
            "tortoise-orm": "Tortoise-ORM",
            "redis": "Redis",
            "celery": "Celery",
            "pytest": "Pytest",
            "djangorestframework": "Django REST Framework",
            "gunicorn": "Gunicorn",
            "psycopg2": "PostgreSQL",
            "psycopg2-binary": "PostgreSQL",
        }
        
        for pkg, lib_name in library_mappings.items():
            if pkg in packages:
                suggestions["libraries"].append(lib_name)
        
        suggestions["libraries"] = list(set(suggestions["libraries"]))
        
    except (FileNotFoundError, Exception) as e:
        pass
    
    return suggestions


def detect_project_context(base_path: str = ".") -> Optional[Dict[str, any]]:
    """
    Main detection function. Scans the project directory and returns suggestions.
    
    Returns:
        Dict with suggested project_type, tech_stack, and libraries, or None if nothing detected
    """
    detected_files = detect_project_files(base_path)
    
    if not detected_files:
        return None
    
    # Prioritize certain files
    priority_files = ["package.json", "requirements.txt", "go.mod", "Cargo.toml", "pubspec.yaml"]
    detected_priority = [f for f in detected_files if any(pf in f[0] for pf in priority_files)]
    
    if detected_priority:
        detected_files = detected_priority
    
    # Analyze the first detected file (or highest priority)
    file_path, detection_key = detected_files[0]
    detection_config = DETECTION_MAPPINGS.get(detection_key, {})
    
    suggestions = {
        "project_type": detection_config.get("project_type"),
        "tech_stack": None,
        "libraries": []
    }
    
    # Deep analysis for specific file types
    if detection_key == "package.json":
        package_analysis = analyze_package_json(file_path)
        suggestions["tech_stack"] = package_analysis.get("tech_stack")
        suggestions["libraries"] = package_analysis.get("libraries", [])
    elif detection_key == "requirements.txt":
        req_analysis = analyze_requirements_txt(file_path)
        suggestions["tech_stack"] = req_analysis.get("tech_stack")
        suggestions["libraries"] = req_analysis.get("libraries", [])
    elif detection_key == "go.mod":
        # Simple detection for Go
        suggestions["tech_stack"] = "Go (Gin)"  # Default assumption
    elif detection_key == "Cargo.toml":
        suggestions["tech_stack"] = "Rust (Clap)"
    elif detection_key == "pubspec.yaml":
        suggestions["tech_stack"] = "Flutter"
    elif "android" in detection_key:
        suggestions["tech_stack"] = "Kotlin (Android)"
    elif "ios" in detection_key:
        suggestions["tech_stack"] = "Swift (iOS)"
    elif "electron" in detection_key:
        suggestions["tech_stack"] = "Electron"
    elif "tauri" in detection_key:
        suggestions["tech_stack"] = "Tauri"
    elif detection_key == "Dockerfile" or "docker" in detection_key:
        suggestions["tech_stack"] = "Docker"
    elif detection_key == "k8s":
        suggestions["tech_stack"] = "Kubernetes"
    elif detection_key == "*.tf":
        suggestions["tech_stack"] = "Terraform"
    
    # If tech_stack not determined, use first candidate
    if not suggestions["tech_stack"] and detection_config.get("tech_stack_candidates"):
        suggestions["tech_stack"] = detection_config["tech_stack_candidates"][0]
    
    return suggestions

