# 🗺️ Product Roadmap

This document outlines the development plan for **PAPER-CODE**.

## 📍 Phase 1: MVP (Core Foundation) - ✅ Completed

- [x] **Core Engine:** Jinja2 templating system.
- [x] **CLI Interface:** Interactive prompts using `Typer` & `Inquirer`.
- [x] **Configuration:** Centralized `src/config.py`.
- [x] **Base Templates:**
  - [x] Core (README, LICENSE, etc.)
  - [x] AI Rules (Cursor, Copilot, Windsurf).
  - [x] Frontend Stacks (React, Vue, Next.js, etc.).
  - [x] Backend Stacks (Node, Python, Go).
  - [x] Libraries (Axios, TailwindCSS, etc.).
  - [x] .github folder (CI/CD, PR templates, Copilot instructions).

## 📍 Phase 2: Enhanced Developer Experience - ✅ Completed

- [x] **Rich UI:** Replace standard print statements with `Rich` (tables, spinners, colored outputs).
- [x] **Smart Detection:** Automatically detect `package.json` or `requirements.txt` to suggest stacks if running in an existing folder.
- [x] **Batch Mode:** Support generating docs from a `paper.config.json` file (Infrastructure as Code).
- [x] **More Templates:**
  - [x] DevOps (Docker, K8s, Terraform).
  - [x] Mobile (Kotlin, Swift native).

## 📍 Phase 3: AI Integration & Customization

- [x] **LLM Integration:** Connect to OpenAI API to write the "Project Description" based on a short summary.
- [x] **Custom Templates:** Allow users to point to a local folder of `.j2` templates (`--template-dir ./my-custom-templates`).
- [x] **Update Mode:** Ability to update existing `AI_RULES.md` without overwriting custom changes (intelligent merge).

## 📍 Phase 4: Ecosystem

- [x] **Web GUI:** A simple web interface to generate docs visually.
- [x] **Official Documentation Site:** Using VitePress.
  - [x] Comprehensive guide for users
  - [x] Tech stack documentation (50+ stacks)
  - [x] Library guides (100+ libraries)
  - [x] API reference documentation
  - [x] Architecture guide for developers
  - [x] Contributing guidelines

## 📍 Phase 5: Advanced Features (Future)

- [ ] **Template Marketplace:** Community template repository
- [ ] **Diff Viewer:** Visual comparison of changes in update mode
- [ ] **Webhook Integration:** GitHub integration for auto-updates
- [ ] **Multi-language Support:** Documentation in multiple languages
- [ ] **CLI Plugins:** Extension system for custom commands
- [ ] **Analytics Dashboard:** Usage analytics and insights
