# Features

PAPER-CODE provides a comprehensive suite of features to streamline documentation generation for modern development projects.

## 🤖 AI-First Context

Generate intelligent `.cursorrules` and prompt instructions that are specific to your tech stack. Instead of generic AI rules, PAPER-CODE creates strict coding standards that keep Cursor, Copilot, and Windsurf from hallucinating or using deprecated syntax.

**Benefits:**

- Type-safe code generation
- Framework-specific best practices
- Automatic enforcement of coding standards
- AI-optimized context for better code suggestions

## 🎯 Multi-Stack Support

Support for 50+ pre-built tech stacks across multiple categories:

### Frontend Stacks

- React, Vue, Angular, Next.js, Nuxt, SvelteKit, Remix, Astro

### Backend Stacks

- Node.js/Express, NestJS, Python/FastAPI, Python/Django, Go/Gin, Ruby on Rails

### Mobile Stacks

- React Native, Flutter, Kotlin, Swift, Xamarin

### Other Stacks

- Game Dev (Godot, Unreal Engine), ML/Data Science, DevOps, CLI Tools

## 📚 Library Awareness

Comprehensive documentation templates for 100+ popular libraries:

**State Management:** Redux, Zustand, Jotai, Pinia, Context API  
**Data Fetching:** TanStack Query, Axios, SWR, Fetch API  
**UI & Styling:** TailwindCSS, shadcn/ui, Material UI, Bootstrap  
**Database & ORM:** Prisma, SQLAlchemy, Mongoose, TypeORM, Django ORM  
**DevOps & Infra:** Docker, Kubernetes, Terraform, AWS CDK, Azure IaC

## 🛡️ Governance Ready

Auto-generates professional governance documents:

- **LICENSE:** Multiple license options (MIT, Apache 2.0, GPL, etc.)
- **CHANGELOG.md:** Versioning and release notes template
- **SECURITY.md:** Security reporting guidelines
- **CONTRIBUTING.md:** Contribution guidelines for your stack
- **CODE_STANDARDS.md:** Enforced coding standards
- **GitHub Issue Templates:** Bug reports, feature requests, documentation

## 🔄 Safe Update Mode

Intelligently update existing documentation without losing your custom changes:

```bash
paper-code update --project ./my-project
```

PAPER-CODE analyzes your existing files and merges updates while preserving:

- Custom sections you've added
- Modified code examples
- Project-specific guidelines
- Team conventions

## 📁 Custom Templates

Point to your own template directory for organization-specific standards:

```bash
paper-code --template-dir ./corporate-templates
```

Your templates can use Jinja2 templating with access to:

- Project metadata
- Selected tech stacks
- Libraries configuration
- Custom variables

## 💻 Multiple Interfaces

### Command Line Interface

Interactive wizard with rich terminal UI, spinners, and colored output.

```bash
paper-code init
```

### Batch Mode (Infrastructure as Code)

Generate documentation from a JSON configuration file for CI/CD pipelines.

```bash
paper-code generate --config paper.config.json
```

### Web GUI

Visual configuration interface for visual learners.

```bash
paper-code web
```

## 🚀 LLM Integration

Connect to OpenAI API to generate intelligent project descriptions:

```bash
export OPENAI_API_KEY=sk-...
paper-code init --ai-generate
```

Features:

- Context-aware project descriptions
- AI analyzes your tech stack for better descriptions
- Optional custom hints for additional context
- Fallback to manual entry if API is unavailable

## 🧪 Smart Detection

When running in an existing project directory, PAPER-CODE automatically detects:

- `package.json` → suggests JavaScript/Node frameworks
- `requirements.txt` → suggests Python frameworks
- `go.mod` → suggests Go frameworks
- `Cargo.toml` → suggests Rust frameworks
- `.flutter` → suggests Flutter

## 🔧 Extensibility

PAPER-CODE is built for extensibility:

- Add new stacks by updating config and creating templates
- Extend existing stacks with library-specific documentation
- Create organization-specific template packages
- Contribute templates to the official repository

## 📦 Version Management

Track template versions and compatibility:

- Semantic versioning for templates
- Automatic detection of outdated templates
- Upgrade paths for breaking changes
- Changelog generation for template updates
