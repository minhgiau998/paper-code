<div align="center">

# 📄 PAPER-CODE

**The AI-Native Documentation Generator**

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![PyPI Version](https://img.shields.io/pypi/v/paper-code?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/paper-code/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/paper-code?style=for-the-badge&logo=python&logoColor=white)](https://pypi.org/project/paper-code/)
[![PyPI Status](https://img.shields.io/pypi/status/paper-code?style=for-the-badge)](https://pypi.org/project/paper-code/)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000?style=for-the-badge)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](docs/CONTRIBUTING.md)
[![Version](https://img.shields.io/badge/version-0.5.0-blue?style=for-the-badge)](https://github.com/minhgiau998/paper-code/releases/tag/v0.5.0)

> **Stop writing boilerplate docs.**
> Automatically generate **AI Context**, **Architecture Guides**, and **Governance Files** optimized for Cursor, Windsurf, and Copilot.

[✨ Features](#-features) • [🚀 Installation](#-installation) • [📖 Usage](#-usage) • [� Docs](https://paper-code-docs.vercel.app) • [�🗺️ Roadmap](ROADMAP.md)

</div>

---

## 🎬 Demo

<div align="center">

[![PAPER-CODE Demo](https://asciinema.org/a/766262.svg)](https://asciinema.org/a/766262)

_Watch PAPER-CODE generate AI-ready documentation in seconds_

</div>

---

## 🧐 Why PAPER-CODE?

In the era of AI coding, **Context is King**.
If you ask an AI to "build a feature" without context, it generates generic, legacy code.

**PAPER-CODE** solves this by bootstrapping a robust documentation structure that serves two masters:

1.  **For AI Agents:** Generates `.cursorrules`, `AI_RULES.md`, and strict coding standards to keep your AI (Cursor/Copilot) from hallucinating or using deprecated syntax.
2.  **For Humans:** Creates professional `ARCHITECTURE.md`, `CONTRIBUTING.md`, and tech stack guides so your team stays on the same page.

## ✨ Features

- **🤖 AI-First Context:** Auto-generates `.cursorrules` and prompt instructions tailored to your specific stack (e.g., "Use Next.js App Router, not Pages").
- **🧠 AI-Powered Descriptions:** Generate intelligent project descriptions using OpenAI API with context-aware analysis of your tech stack and libraries.
- **🎯 Multi-Stack Support:** Specialized templates for Frontend, Backend, Mobile, Game Dev, ML, DevOps, and CLI applications.
- **📚 Library Awareness:** Smart docs for 30+ libraries (Tailwind, Prisma, Redux, Zod, Docker, Kubernetes, etc.).
- **🛡️ Governance Ready:** Generates `LICENSE`, `CHANGELOG.md`, `SECURITY.md`, and GitHub Issue Templates.
- **🔄 Safe Update Mode:** Intelligently update existing documentation without overwriting custom changes.
- **📁 Custom Templates:** Support for custom template directories to match your organization's standards.
- **💻 Interactive & Batch:** Use the beautiful CLI wizard or a JSON config file for automation.

## 🚀 Installation

Requires **Python 3.10+**.

### 1. Via PyPI (Recommended)

You can install **PAPER-CODE** directly from PyPI:

```bash
pip install paper-code
```

### Upgrade (From PyPI)

To upgrade an existing system-wide or virtualenv installation of `paper-code` from PyPI to the latest released version:

```bash
# Upgrade to the latest version
pip install --upgrade paper-code

# Or to install a specific version (e.g., 0.1.0)
pip install paper-code==0.1.0
```

### 2. From Source (For Development)

If you want to contribute or use the latest development version:

```bash
# Clone the repository
git clone https://github.com/minhgiau998/paper-code.git
cd paper-code

# Install as an editable tool
pip install -e .
```

## 📖 Usage

### 1. Interactive Mode (Recommended)

Just run the command and follow the wizard.

```bash
paper-code
```

### 2. AI-Powered Description Generation

For enhanced project descriptions, set up your OpenAI API key:

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=your_actual_api_key_here

# Generate docs with AI-powered descriptions
paper-code --ai-generate

# Or provide additional context for better AI descriptions
paper-code --ai-generate --ai-hint "This is an e-commerce platform with real-time inventory"
```

**Terminal Output Preview:**

```text
🚀 Initializing documentation for: My Awesome Project
[?] Select Project Type: Frontend
[?] Select Frontend Stack: Next.js
[?] Select Modules/Libraries: [x] TailwindCSS, [x] Prisma, [x] NextAuth.js, [x] Zod
🤖 Generating AI-powered project description...
✅ AI description generated successfully!

✨ Done! Generated AI-ready docs in ./output
```

### 3. Custom Templates

Use your own template directory:

```bash
paper-code --template-dir ./my-custom-templates
```

Your custom templates should follow the same structure as the default templates:

```
my-custom-templates/
├── core/
│   ├── README.md.j2
│   ├── LICENSE.j2
│   └── ...
├── ai/
│   ├── AI_RULES.md.j2
│   └── ...
└── stacks/
    └── frontend/
        └── nextjs_arch.md.j2
```

### 4. Update Mode

Update existing documentation without losing custom changes:

```bash
paper-code --update --template Frontend --tech-stack Next.js
```

Update mode:

- ✅ Preserves custom sections in `AI_RULES.md`
- ✅ Merges existing `ARCHITECTURE.md` content
- ✅ Skips user-modified files (README.md, CONTRIBUTING.md, etc.)

### 5. Quick Start (Templates)

Skip the questions if you know what you want.

```bash
paper-code --template "Next.js" --output ./my-app
paper-code --template "FastAPI" --output ./my-api
```

### 6. Batch Mode (For CI/CD)

Generate docs based on a configuration file.

```bash
paper-code --config paper.config.json --batch
```

## 🧩 Supported Stacks

**PAPER-CODE** isn't just generic markdown. It contains deep, opinionated knowledge for:

| Category      | Supported Stacks                                                |
| :------------ | :-------------------------------------------------------------- |
| **Frontend**  | React, Vue, Next.js, Nuxt.js, Angular, Svelte                   |
| **Backend**   | Node.js (Express/NestJS/Fastify), FastAPI, Django, Go (Gin)     |
| **Mobile**    | React Native (Expo/CLI), Flutter, Kotlin (Android), Swift (iOS) |
| **Desktop**   | Electron, Tauri                                                 |
| **Data & ML** | PyTorch, TensorFlow, Scikit-learn                               |
| **Game Dev**  | Godot, Unity                                                    |
| **CLI**       | Node.js (Commander), Python (Click), Go (Cobra), Rust (Clap)    |
| **Libraries** | TypeScript Lib, Python Lib, Go Lib, Rust Lib                    |
| **DevOps**    | Docker, Kubernetes, Terraform                                   |

## 📂 Generated Structure

A typical **Next.js + Prisma** project generated by PAPER-CODE:

```text
my-project/
├── .cursorrules             # 👈 Critical for AI Editors
├── .github/
│   ├── copilot-instructions.md
│   └── workflows/ci.yml
├── docs/
│   ├── ai/
│   │   ├── AI_RULES.md      # The "Constitution" for your AI
│   │   ├── AI_WORKFLOWS.md  # SOPs for common tasks
│   │   └── AI_CONTEXT.md    # Project map
│   ├── libs/                # Specific guides for libraries
│   │   ├── prisma.md
│   │   └── tailwindcss.md
│   ├── ARCHITECTURE.md
│   ├── CODE_STANDARDS.md    # "Do's and Don'ts"
│   ├── CONTRIBUTING.md
│   └── TESTING.md
├── CHANGELOG.md
└── README.md
```

## 🤝 Contributing

We love contributions! Whether it's adding a new Tech Stack template or fixing a typo.
Please read our [CONTRIBUTING.md](docs/CONTRIBUTING.md) to get started.

1.  Fork the repo.
2.  Create your feature branch (`git checkout -b feature/amazing-stack`).
3.  Commit your changes (`git commit -m 'feat: add Astro support'`).
4.  Push to the branch.
5.  Open a Pull Request.

## � Publishing & Releases

PAPER-CODE is published to PyPI and automatically deployed on every release.

### For Maintainers

See [PUBLISHING.md](PUBLISHING.md) for detailed instructions on:

- Preparing releases
- Publishing to PyPI
- Version management
- Release verification

Quick publish:

```bash
# 1. Update version in pyproject.toml
# 2. Create and push git tag
git tag v0.6.0
git push origin --tags

# 3. GitHub Actions automatically publishes to PyPI
# 4. Verify at https://pypi.org/project/paper-code/
```

### Check Package Status

- **PyPI Package:** https://pypi.org/project/paper-code/
- **Download Stats:** https://pypistats.org/packages/paper-code
- **Latest Release:** https://github.com/minhgiau998/paper-code/releases

## �📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

<div align="center">
  <sub>Built with ❤️ by Developers, for Developers (and their AI assistants).</sub>
</div>
