# CLI Usage

Comprehensive guide to using PAPER-CODE from the command line.

## Interactive Mode

The most user-friendly way to generate documentation.

```bash
paper-code init
```

This launches an interactive wizard that guides you through:

1. Project name
2. Project type selection
3. Tech stack selection
4. Library/module selection
5. Output directory

## Command-Line Flags

Generate documentation without interactive prompts:

```bash
paper-code init \
  --name "My Project" \
  --type frontend \
  --stack "React" \
  --libraries "TypeScript,TailwindCSS,Redux" \
  --output ./docs
```

### Available Flags

| Flag             | Description                | Example                                |
| ---------------- | -------------------------- | -------------------------------------- |
| `--name`         | Project name               | `--name "My App"`                      |
| `--type`         | Project type               | `--type frontend`                      |
| `--stack`        | Tech stack                 | `--stack "React"`                      |
| `--libraries`    | Comma-separated libraries  | `--libraries "TypeScript,TailwindCSS"` |
| `--output`       | Output directory           | `--output ./output`                    |
| `--template-dir` | Custom templates directory | `--template-dir ./templates`           |
| `--ai-generate`  | Generate with AI           | `--ai-generate`                        |
| `--ai-hint`      | Additional context for AI  | `--ai-hint "E-commerce platform"`      |

## Batch Mode (Infrastructure as Code)

Generate documentation from a configuration file for automation:

```bash
paper-code generate --config paper.config.json
```

### Configuration File Format

Create `paper.config.json`:

```json
{
  "projects": [
    {
      "name": "Frontend App",
      "type": "frontend",
      "stack": "React",
      "libraries": ["TypeScript", "TailwindCSS", "TanStack Query"],
      "output": "./frontend-docs"
    },
    {
      "name": "Backend API",
      "type": "backend",
      "stack": "NestJS",
      "libraries": ["TypeScript", "Prisma", "PostgreSQL"],
      "output": "./backend-docs"
    }
  ]
}
```

This is perfect for:

- CI/CD pipelines
- Monorepo documentation
- Multi-project initialization
- Automated documentation updates

## Update Mode

Update existing documentation while preserving custom changes:

```bash
paper-code update --project ./my-project
```

PAPER-CODE will:

1. Detect existing documentation
2. Analyze custom modifications
3. Merge template updates
4. Preserve your changes

## AI-Powered Features

### Generate with AI Descriptions

```bash
export OPENAI_API_KEY=sk-...
paper-code init --ai-generate
```

### With Context Hints

```bash
paper-code init \
  --ai-generate \
  --ai-hint "Real-time inventory system with multi-tenant support"
```

## Project Type Reference

### Frontend

- React, Vue, Angular, Next.js, Nuxt, SvelteKit, Remix, Astro

### Backend

- Node.js/Express, NestJS, FastAPI, Django, Go, Ruby on Rails

### Mobile

- React Native, Flutter, Kotlin, Swift

### Other

- Game Dev, ML/Data Science, DevOps, CLI Tools

## Stack-Specific Options

After selecting a project type, available stacks vary. Examples:

**Frontend Stacks:**

```bash
paper-code init --type frontend --stack "React"
paper-code init --type frontend --stack "Next.js"
paper-code init --type frontend --stack "Vue"
```

**Backend Stacks:**

```bash
paper-code init --type backend --stack "NestJS"
paper-code init --type backend --stack "FastAPI"
paper-code init --type backend --stack "Express"
```

## Helpful Commands

### View Help

```bash
paper-code --help
```

### View Version

```bash
paper-code --version
```

### List Available Stacks

```bash
paper-code stacks
```

### List Available Libraries

```bash
paper-code libraries
```

## Tips & Tricks

### Scripting Documentation Generation

Create a bash script for consistent initialization:

```bash
#!/bin/bash
PROJECT_NAME=$1
PROJECT_TYPE=$2
TECH_STACK=$3

paper-code init \
  --name "$PROJECT_NAME" \
  --type "$PROJECT_TYPE" \
  --stack "$TECH_STACK" \
  --output "./output"
```

Usage:

```bash
./generate-docs.sh "My App" "frontend" "React"
```

### Using with Git Hooks

Generate docs on pre-commit:

```bash
# .git/hooks/pre-commit
paper-code update --project .
git add docs/
```

### Monorepo Approach

Use batch mode for monorepos:

```bash
paper-code generate --config monorepo-config.json
```

Then commit all generated docs to version control.
