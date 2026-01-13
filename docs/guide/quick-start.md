# Quick Start

Create your first AI-ready documentation in less than 5 minutes.

## Basic Usage

### Step 1: Run the Initialization Wizard

```bash
paper-code init
```

### Step 2: Follow the Interactive Prompts

The wizard will ask you:

1. **Project Name:** What is your project called?
2. **Project Type:** Is it Frontend, Backend, Mobile, DevOps, or something else?
3. **Tech Stack:** Which framework/language are you using?
4. **Libraries:** Which libraries and tools are you using?
5. **Output Directory:** Where should the docs be generated?

### Step 3: Review Generated Files

PAPER-CODE will generate:

```
output/
├── README.md                    # Professional project README
├── CHANGELOG.md                 # Version history template
├── LICENSE                      # License file
├── SECURITY.md                  # Security guidelines
├── CONTRIBUTING.md              # Contribution guidelines
├── .gitignore                   # Git ignore rules
├── .cursorrules                 # Cursor AI rules
├── docs/
│   ├── ARCHITECTURE.md          # Architecture guide (stack-specific)
│   ├── CODE_STANDARDS.md        # Coding standards for your stack
│   ├── TESTING.md               # Testing strategies
│   ├── DEPLOYMENT.md            # Deployment guide
│   ├── SECURITY.md              # Security best practices
│   ├── ai/
│   │   ├── AI_CONTEXT.md        # AI agent context
│   │   ├── AI_RULES.md          # Rules for AI coding assistants
│   │   └── AI_WORKFLOWS.md      # Recommended workflows
│   └── libs/
│       └── [library-specific docs]
└── .github/
    ├── workflows/
    │   └── ci.yml               # CI/CD workflow
    └── PULL_REQUEST_TEMPLATE.md # PR template
```

## Example: React + TypeScript

```bash
$ paper-code init
🚀 PAPER-CODE - AI-Native Documentation Generator

Project Name: My React App
Project Type: Frontend
Tech Stack: React
Select Modules/Libraries:
  [x] TypeScript
  [x] TailwindCSS
  [x] TanStack Query
  [x] Zustand
  [x] Jest

Output Directory: ./output

✨ Generated documentation successfully!
```

Now your `output/` directory contains a complete documentation suite tailored to React development.

## Using the Generated Files

### For Your Team

1. **README.md** → Share with team and stakeholders
2. **CONTRIBUTING.md** → Onboard new developers
3. **docs/ARCHITECTURE.md** → Understand the project structure
4. **docs/CODE_STANDARDS.md** → Follow coding conventions

### For AI Coding Assistants

1. Add `.cursorrules` to root of your project
2. Share `docs/ai/AI_RULES.md` with your team
3. Use `docs/ai/AI_CONTEXT.md` in Cursor/Copilot chats

### For CI/CD

1. Use `.github/workflows/ci.yml` as a starting point
2. Customize for your repository
3. Add to your GitHub Actions

## Command-Line Options

Generate without interactive prompts:

```bash
paper-code init \
  --name "My App" \
  --type frontend \
  --stack "React" \
  --libraries "TypeScript,TailwindCSS,TanStack Query" \
  --output ./docs
```

## Next Steps

- Learn about [Tech Stacks](/stacks/)
- Explore [Available Libraries](/libraries/)
- Discover [Advanced Features](/guide/ai-generation)
- Check out [Batch Mode](/guide/batch-mode) for automation
