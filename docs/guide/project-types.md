# Project Types

Learn about the different project types supported by PAPER-CODE.

## Frontend Projects

Web applications built with modern frontend frameworks.

### Supported Stacks

- React (with TypeScript, Redux, Zustand, etc.)
- Vue (with Vuex, Pinia, TypeScript)
- Angular (with TypeScript, RxJS)
- Next.js (with TypeScript, Prisma, NextAuth)
- Nuxt (with TypeScript, Composition API)
- SvelteKit (with TypeScript, Adapter)
- Remix (with TypeScript, Loaders, Actions)
- Astro (with Integrations, Components)

### Use This Type When

- Building web applications in the browser
- Creating Single Page Applications (SPAs)
- Developing static sites or hybrid sites

## Backend Projects

Server-side applications and APIs.

### Supported Stacks

- Node.js/Express (with TypeScript, Middleware)
- NestJS (with TypeScript, Modules, Guards)
- FastAPI (with Python, Async, Validators)
- Django (with Python, ORM, Admin)
- Go (with Gin, Chi, Echo)
- Ruby on Rails

### Use This Type When

- Building REST or GraphQL APIs
- Creating microservices
- Developing backend servers
- Building CLI applications

## Mobile Projects

Native and cross-platform mobile applications.

### Supported Stacks

- React Native (with TypeScript, Navigation)
- Flutter (with Dart, Riverpod)
- Kotlin (with Jetpack Compose, Room)
- Swift (with SwiftUI, Core Data)

### Use This Type When

- Building iOS/Android applications
- Creating cross-platform mobile apps
- Developing native mobile experiences

## Game Development

Video game projects using popular engines.

### Supported Stacks

- Godot (with GDScript, C#)
- Unreal Engine (with C++, Blueprints)
- Unity (with C#, Asset Store)

### Use This Type When

- Developing video games
- Creating game prototypes
- Building interactive experiences

## DevOps & Infrastructure

Infrastructure-as-Code and deployment configurations.

### Supported Stacks

- Docker (with Compose, Multi-stage)
- Kubernetes (with Helm, Kustomize)
- Terraform (with AWS, Azure, GCP)
- CI/CD (GitHub Actions, GitLab CI)

### Use This Type When

- Setting up containerization
- Managing Kubernetes clusters
- Infrastructure provisioning
- Setting up CI/CD pipelines

## Data Science & ML

Machine Learning and data analysis projects.

### Supported Stacks

- Python/FastAPI (with TensorFlow, PyTorch)
- Python/Django (with scikit-learn, pandas)
- Jupyter Notebooks (with Matplotlib, Seaborn)

### Use This Type When

- Building ML models
- Data analysis and visualization
- Research projects
- Data pipelines

## CLI Tools

Command-line applications and tools.

### Supported Stacks

- Python (with Click, Typer)
- Node.js (with Commander, Yargs)
- Go (with Cobra, Cli)
- Rust (with Clap)

### Use This Type When

- Building CLI applications
- Creating developer tools
- Building system utilities

## Monorepo

Multi-project repositories with shared tooling.

### Supported Stacks

- Nx (with TypeScript)
- Turborepo (with npm/yarn workspaces)
- Lerna (with npm packages)
- pnpm Workspaces

### Use This Type When

- Managing multiple related projects
- Sharing code across projects
- Coordinating deployments

## Choosing a Project Type

1. **Identify your primary output:** What is the deliverable?
2. **Select matching type:** Choose the closest category
3. **Pick specific stack:** Choose your framework/language
4. **Add libraries:** Select tools and utilities

### Decision Tree

```
What are you building?
├─ Web Application in Browser → Frontend
├─ API/Server Backend → Backend
├─ Mobile Application → Mobile
├─ Video Game → Game Development
├─ ML Model/Data Analysis → Data Science
├─ Infrastructure/Deployment → DevOps
├─ Command-line Tool → CLI
└─ Multiple Projects → Monorepo
```

## Changing Project Type

You can regenerate documentation with a different project type:

```bash
paper-code init --type backend --stack "NestJS"
```

This will create a new set of documentation optimized for backend development.
