# Changelog

All notable changes to **PAPER-CODE** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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