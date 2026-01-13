# Batch Mode (Infrastructure as Code)

Generate documentation for multiple projects from a JSON configuration file for automation and CI/CD integration.

## Overview

Batch mode allows you to define all your projects in a single configuration file and generate documentation for all of them at once. This is perfect for:

- Monorepos with multiple packages
- CI/CD pipelines
- Automated documentation generation
- Version control and reproducibility
- Team consistency

## Configuration File

Create a `paper.config.json` file in your project root:

```json
{
  "version": "1.0",
  "projects": [
    {
      "name": "Frontend App",
      "type": "frontend",
      "stack": "React",
      "libraries": ["TypeScript", "TailwindCSS", "TanStack Query"],
      "output": "./docs/frontend"
    },
    {
      "name": "Backend API",
      "type": "backend",
      "stack": "NestJS",
      "libraries": ["TypeScript", "Prisma", "PostgreSQL"],
      "output": "./docs/backend"
    }
  ]
}
```

## Basic Usage

Generate all projects from configuration:

```bash
paper-code generate --config paper.config.json
```

Output:

```
✨ Generating documentation for 2 projects...
  ✅ Frontend App → docs/frontend
  ✅ Backend API → docs/backend
Done!
```

## Configuration Schema

### Root Level

| Property      | Type    | Required | Description                               |
| ------------- | ------- | -------- | ----------------------------------------- |
| `version`     | string  | No       | Config format version (default: "1.0")    |
| `projects`    | array   | Yes      | Array of project configurations           |
| `templateDir` | string  | No       | Custom template directory                 |
| `overwrite`   | boolean | No       | Overwrite existing files (default: false) |

### Project Level

| Property      | Type    | Required | Description                                    |
| ------------- | ------- | -------- | ---------------------------------------------- |
| `name`        | string  | Yes      | Project name                                   |
| `type`        | string  | Yes      | Project type (frontend, backend, mobile, etc.) |
| `stack`       | string  | Yes      | Tech stack                                     |
| `libraries`   | array   | No       | Array of library/tool names                    |
| `output`      | string  | Yes      | Output directory                               |
| `description` | string  | No       | Project description                            |
| `aiGenerate`  | boolean | No       | Generate description with AI                   |
| `aiHint`      | string  | No       | Context hint for AI generation                 |
| `templateDir` | string  | No       | Override global template directory             |

## Advanced Examples

### Multi-Stack Monorepo

```json
{
  "projects": [
    {
      "name": "Web Dashboard",
      "type": "frontend",
      "stack": "Next.js",
      "libraries": ["TypeScript", "TailwindCSS", "Prisma Client"],
      "output": "./apps/web/docs",
      "description": "Customer-facing analytics dashboard"
    },
    {
      "name": "Mobile App",
      "type": "mobile",
      "stack": "React Native",
      "libraries": ["TypeScript", "Redux Toolkit", "React Navigation"],
      "output": "./apps/mobile/docs",
      "description": "iOS and Android companion app"
    },
    {
      "name": "API Server",
      "type": "backend",
      "stack": "NestJS",
      "libraries": ["TypeScript", "Prisma", "JWT", "Docker"],
      "output": "./apps/api/docs",
      "description": "Core REST API and microservices"
    },
    {
      "name": "Infrastructure",
      "type": "devops",
      "stack": "Kubernetes",
      "libraries": ["Docker", "Terraform", "Helm"],
      "output": "./infrastructure/docs",
      "description": "Kubernetes cluster and deployment configuration"
    }
  ]
}
```

### With AI Generation

```json
{
  "projects": [
    {
      "name": "Analytics Engine",
      "type": "backend",
      "stack": "Python/FastAPI",
      "libraries": ["TensorFlow", "Pandas", "PostgreSQL"],
      "output": "./docs/analytics",
      "aiGenerate": true,
      "aiHint": "Real-time data processing pipeline with ML model inference"
    }
  ]
}
```

### With Custom Templates

```json
{
  "templateDir": "./corporate-templates",
  "projects": [
    {
      "name": "Project 1",
      "type": "frontend",
      "stack": "React",
      "output": "./project1/docs"
    }
  ]
}
```

## CI/CD Integration

### GitHub Actions

```yaml
name: Generate Documentation

on:
  push:
    branches: [main]
    paths:
      - "paper.config.json"

jobs:
  generate-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      - name: Install paper-code
        run: pip install paper-code

      - name: Generate documentation
        run: paper-code generate --config paper.config.json

      - name: Commit changes
        run: |
          git config user.name "Documentation Bot"
          git config user.email "bot@example.com"
          git add docs/
          git commit -m "docs: auto-generate documentation" || true
          git push
```

### GitLab CI

```yaml
generate-docs:
  image: python:3.10
  script:
    - pip install paper-code
    - paper-code generate --config paper.config.json
  artifacts:
    paths:
      - docs/
  only:
    - main
```

## Pre-Commit Hook

Automatically generate docs before committing:

```bash
#!/bin/bash
# .git/hooks/pre-commit

if [ -f paper.config.json ]; then
  paper-code generate --config paper.config.json
  git add docs/
fi
```

Install hook:

```bash
chmod +x .git/hooks/pre-commit
```

## Validation

Validate configuration before generation:

```bash
paper-code validate --config paper.config.json
```

Output:

```
✅ Configuration is valid
  - 3 projects defined
  - All required fields present
  - All stacks are supported
  - Output directories are writable
```

## Dry Run

Preview generation without writing files:

```bash
paper-code generate --config paper.config.json --dry-run
```

Output:

```
📋 Dry run - no files will be written

Project 1: Frontend App
  Files to generate:
    ✓ docs/frontend/README.md
    ✓ docs/frontend/ARCHITECTURE.md
    ✓ docs/frontend/.cursorrules
    ...

Project 2: Backend API
  Files to generate:
    ✓ docs/backend/README.md
    ...
```

## Error Handling

### Partial Failures

If one project fails, others continue:

```
✨ Generating documentation...
  ✅ Frontend App
  ❌ Backend API (Stack 'InvalidStack' not supported)
  ✅ Infrastructure

⚠️  2 succeeded, 1 failed
```

### Retry on Failure

```bash
# Retry failed projects only
paper-code generate --config paper.config.json --retry
```

## Monitoring & Logging

### Verbose Output

```bash
paper-code generate --config paper.config.json --verbose
```

### Log File

```bash
paper-code generate --config paper.config.json --log docs-generation.log
```

## Environment Variables

Override configuration with environment variables:

```bash
export PAPER_CODE_TEMPLATE_DIR=/opt/templates
export PAPER_CODE_OVERWRITE=true
paper-code generate --config paper.config.json
```

## Versioning Configuration

Keep configuration in version control:

```bash
git add paper.config.json
git commit -m "docs: update documentation configuration"
```

Track changes to documentation generation:

```bash
git log paper.config.json
```

## Best Practices

1. **Keep Configuration DRY:** Use global defaults when possible
2. **Organize by Package:** Use logical output directory structure
3. **Version Control:** Commit `paper.config.json` to git
4. **CI/CD Pipeline:** Automate in your build process
5. **Validation:** Validate configuration regularly
6. **Documentation:** Document your configuration choices

## Example Repository Structure

```
my-monorepo/
├── paper.config.json          # Configuration
├── apps/
│   ├── web/
│   │   ├── docs/              # Generated docs
│   │   └── package.json
│   ├── mobile/
│   │   ├── docs/              # Generated docs
│   │   └── package.json
│   └── api/
│       ├── docs/              # Generated docs
│       └── package.json
├── .github/workflows/
│   └── docs.yml               # CI/CD workflow
└── .git/hooks/
    └── pre-commit             # Git hook
```

## Troubleshooting

### Config file not found

```bash
# Make sure file exists in current directory
ls paper.config.json

# Or specify full path
paper-code generate --config /path/to/paper.config.json
```

### Invalid JSON

```bash
# Validate JSON syntax
python -m json.tool paper.config.json
```

### Output directory exists

```bash
# Force overwrite
paper-code generate --config paper.config.json --overwrite
```

---

For more information, see the [CLI Usage guide](./cli-usage.md) or [Quick Start](./quick-start.md).
