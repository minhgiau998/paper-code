# Changelog

All notable changes to **PAPER-CODE** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0] - 2026-01-06

### 🎨 Rich UI & Branding
- **Terminal Aesthetics:** Fully integrated `Rich` library for beautiful banners, gradient text, and styled panels.
- **Interactive Feedback:** Added spinners, progress indicators, and colored success messages for a more premium CLI feel.
- **Dynamic Dividers:** Improved CLI layout with clear section dividers and formatted banners.

### 🔍 Smart Project Context Detection
- **Auto-Detection Engine:** Added `detector.py` to automatically identify project types and tech stacks from files like `package.json`, `requirements.txt`, `go.mod`, and `Cargo.toml`.
- **Pre-filled Prompts:** The interactive wizard now suggests the most likely project configuration, reducing setup time.
- **Deep Dependency Analysis:** Analyzes dependencies to automatically suggest documentation for specific libraries (e.g., detecting `Prisma` in `package.json`).

### 📂 Expanded Template Ecosystem (Phase 2)
- **DevOps Stacks:** New documentation templates for Docker (Compose, Multi-stage), Kubernetes (Helm, Kustomize), and Terraform (AWS/Azure/GCP providers).
- **Mobile Native:** Added specialized coding standards and architecture guides for Kotlin (Android) and Swift (iOS).
- **Batch Mode Refinement:** Improved reliability of non-interactive document generation via `paper.config.json`.

### ⚙️ Engine Robustness
- **Modular Detection:** Separated detection logic from the main generator for better maintainability.
- **Enhanced Path Handling:** Improved robust path resolution for across different operating systems.

## [0.2.0] - 2026-01-05

### 🔧 Template Improvements & Robustness
- **Error Handling:** Added `default()` filters to all Jinja2 templates to prevent rendering errors when variables are undefined.
- **Safe Conditionals:** Replaced all unsafe `{% if "X" in libraries %}` patterns with robust `{% if libraries | default([]) | select("in", ["X"]) | list | length > 0 %}` patterns across 80+ template files.
- **Version Updates:** Updated recommended versions in CI/CD and documentation:
  - Node.js: 20.x → 22.x (LTS)
  - Python: 3.10 → 3.12
  - Go: 1.21 → 1.22

### 📚 Enhanced Documentation Templates
- **Core Templates:**
  - Added "Security Checklist" section to `SECURITY.md` with OWASP Top 10 references.
  - Enhanced `TESTING.md` with sections on Test Coverage, Mocking Strategies, E2E Best Practices, and Debugging Tests.
  - Expanded `DEPLOYMENT.md` with Environment Variables, Docker Deployment, Rollback Strategy, and Monitoring & Logging sections.
  - Improved `CONTRIBUTING.md` with Code Review Process and Local Development Setup sections.
- **Architecture Docs:**
  - Added Mermaid data flow diagram to React architecture documentation.
  - Added Performance Optimization section to React standards.
  - Enhanced conditional logic for better library detection across all stack templates.

### 🛡️ Quality Assurance
- **Comprehensive Fixes:** Fixed 76+ unsafe Jinja2 patterns across:
  - Core templates (README, SECURITY, TESTING, DEPLOYMENT, CONTRIBUTING, etc.)
  - AI templates (AI_CONTEXT, AI_RULES, cursorrules, copilot-instructions)
  - Library templates (20+ library docs)
  - Stack templates (Frontend, Backend, Mobile, CLI, Game, Data/ML, Library)
  - GitHub templates (CI/CD workflows)
- **Zero Linting Errors:** All templates pass linting checks and are production-ready.

## [0.1.0] - 2026-01-04

### 🚀 Initial Release
- **PAPER-CODE Launch:** Released the first version of the interactive documentation generator optimized for AI-native development.
- **Interactive CLI:** Implemented a wizard using `typer` and `inquirer` to guide users through project setup.
- **Batch Mode:** Added support for non-interactive generation via JSON config (`--config paper.config.json`).
- **Template Shortcuts:** Added `--template` flag for quick bootstrapping.

### 🤖 AI Context & Governance
- **Editor Integration:** Auto-generation of `.cursorrules` (for Cursor) and `.github/copilot-instructions.md` (for GitHub Copilot).
- **AI Rules:** Added generation of `docs/ai/AI_RULES.md` and `AI_WORKFLOWS.md` to establish strict coding standards for AI agents.
- **Governance Docs:** Automatically creates `ARCHITECTURE.md`, `CONTRIBUTING.md`, `CODE_STANDARDS.md`, `LICENSE`, and `CHANGELOG.md`.

### 🧩 Supported Tech Stacks
- **Frontend:**
  - React (Vite), Vue 3, Svelte.
  - Meta-frameworks: Next.js (App Router), Nuxt.js (v3), SvelteKit.
  - Angular (v17+ Standalone).
- **Backend:**
  - Node.js (Express, NestJS, Fastify).
  - Python (FastAPI, Django).
  - Go (Gin).
- **Mobile:** React Native (Expo & CLI), Flutter.
- **Desktop:** Electron, Tauri (v2).
- **Data & ML:** PyTorch, TensorFlow (Keras 3), Scikit-learn.
- **Game Dev:** Godot 4, Unity (2023 LTS).
- **CLI Tools:** Node.js (Commander), Python (Click), Go (Cobra), Rust (Clap).
- **Libraries:** Templates for building TypeScript, Python, Go, and Rust libraries.

### 📚 Module & Library Integrations
- **Styling:** TailwindCSS (Web/Native), Shadcn UI, Nuxt UI, Angular Material.
- **State Management:** Redux Toolkit, Zustand, Pinia, NgRx.
- **Data & Networking:** Axios, TanStack Query, RxJS, Prisma, Supabase.
- **Validation & Auth:** Zod, NextAuth.js (v5).
- **Routing:** React Router (v6.4), Vue Router.
- **Testing:** Jest, Vitest.
- **i18n:** Support for `next-intl`, `vue-i18n`, and `react-i18next`.

### 🛠️ Core Infrastructure
- **Modern Packaging:** Switched to `pyproject.toml` (PEP 621) compliant packaging (No `setup.py` needed).
- **CI/CD:** Added smart `.github/workflows/ci.yml` generation that adapts to the selected stack.
- **Templates:** Implemented a modular Jinja2 template system for easy extensibility.