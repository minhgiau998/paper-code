# Configuration

Configure PAPER-CODE to match your organization's needs and preferences.

## Environment Variables

### API Key Configuration

```bash
# OpenAI API Key for AI-powered generation
export OPENAI_API_KEY=sk-...

# Optional: Specify different model
export OPENAI_MODEL=gpt-4  # or gpt-3.5-turbo
```

### Tool Configuration

```bash
# Custom templates directory
export PAPER_CODE_TEMPLATE_DIR=/opt/templates

# Disable AI generation
export PAPER_CODE_AI_DISABLED=true

# Set output format
export PAPER_CODE_FORMAT=markdown  # or html, json
```

### Logging

```bash
# Enable verbose logging
export PAPER_CODE_DEBUG=true

# Log file location
export PAPER_CODE_LOG_FILE=/var/log/paper-code.log

# Log level
export PAPER_CODE_LOG_LEVEL=DEBUG  # INFO, WARNING, ERROR
```

## Configuration Files

### .env File

Create `.env` in project root:

```bash
# .env
OPENAI_API_KEY=sk-...
PAPER_CODE_TEMPLATE_DIR=./templates
PAPER_CODE_DEBUG=false
```

Load environment:

```bash
# Automatic (with python-dotenv)
paper-code init

# Or manual
source .env
paper-code init
```

### paper.config.json

Main configuration for batch mode:

```json
{
  "version": "1.0",
  "templateDir": "./templates",
  "overwrite": false,
  "projects": [
    {
      "name": "Project Name",
      "type": "frontend",
      "stack": "React",
      "output": "./docs"
    }
  ]
}
```

## System Configuration

### ~/.paper-code/config.yaml

User-level configuration:

```yaml
# User preferences
defaults:
  project_type: frontend
  stack: React
  output_dir: ./docs

# Template settings
templates:
  custom_dir: ~/paper-code-templates
  cache: true
  cache_expiry: 3600

# AI settings
ai:
  enabled: true
  model: gpt-4
  temperature: 0.7
  max_tokens: 1000

# Logging
logging:
  level: INFO
  format: json
  file: ~/.paper-code/logs/paper-code.log
```

## Project Settings

### paper-code.yaml

Project-level configuration:

```yaml
# Project metadata
project:
  name: My Project
  type: frontend
  stack: React
  author: Your Name
  year: 2024

# Documentation settings
docs:
  output_dir: ./docs
  format: markdown
  include_diagrams: true

# AI settings for this project
ai:
  generate_description: true
  model: gpt-4
  temperature: 0.7

# Custom variables for templates
variables:
  company: "ACME Corp"
  team: "Frontend Team"
  slack_channel: "#frontend"
```

## Advanced Configuration

### Custom Template Directories

Define multiple template sources:

```yaml
templates:
  - name: official
    path: https://github.com/paper-code/official-templates
    version: 1.0.0

  - name: company
    path: ./corporate-templates
    version: 2.0.0
    priority: high
```

### Library Definitions

Customize available libraries:

```json
{
  "libraries": {
    "React": {
      "frontend": ["TypeScript", "TailwindCSS", "Redux Toolkit"]
    },
    "CustomLib": {
      "compatible_with": ["React", "Vue"],
      "documentation": "https://custom.lib/docs"
    }
  }
}
```

### Stack Customization

Add custom stacks:

```json
{
  "stacks": {
    "MyCustomStack": {
      "category": "frontend",
      "extends": "React",
      "libraries": ["TypeScript", "TailwindCSS"],
      "templates": ["custom_arch.md.j2", "custom_standards.md.j2"]
    }
  }
}
```

## Feature Flags

Enable/disable experimental features:

```yaml
features:
  ai_generation: true
  custom_templates: true
  update_mode: true
  batch_mode: true
  webhook_integration: false # Experimental
  template_marketplace: false # Coming soon
```

## Output Customization

### File Generation Options

```json
{
  "output": {
    "include_files": [
      "README.md",
      "ARCHITECTURE.md",
      "CODE_STANDARDS.md",
      ".cursorrules"
    ],
    "exclude_files": [
      "LICENSE"  # Don't generate license
    ],
    "naming_convention": "snake_case"  # or kebab-case, camelCase
  }
}
```

### Directory Structure

```json
{
  "output": {
    "structure": "flat", // flat, nested, custom
    "paths": {
      "readme": "README.md",
      "architecture": "docs/ARCHITECTURE.md",
      "standards": "docs/CODE_STANDARDS.md",
      "ai_rules": ".cursorrules"
    }
  }
}
```

## Git Integration

Configure Git-related settings:

```yaml
git:
  auto_commit: false
  commit_message: "docs: auto-generate documentation"
  branch: main

  # Pre-commit hook
  pre_commit:
    enabled: true
    update_docs: true
```

## CI/CD Integration

Configure for different CI/CD systems:

```yaml
ci_cd:
  provider: github # github, gitlab, jenkins, etc.

  github_actions:
    on_push: true
    on_pull_request: true
    branches: [main, develop]

  gitlab_ci:
    stages: [pre, build, deploy]
    stage: pre
```

## Validation & Linting

Configure validation:

```yaml
validation:
  # Validate markdown
  markdown:
    enabled: true
    check_links: true
    check_references: true

  # Validate templates
  templates:
    enabled: true
    check_jinja_syntax: true

  # Validate JSON
  json:
    enabled: true
    strict_mode: false
```

## Performance Tuning

Optimize for your system:

```yaml
performance:
  # Cache settings
  cache:
    enabled: true
    ttl: 3600
    max_size: 100MB

  # Parallelization
  parallel:
    enabled: true
    workers: 4

  # Template compilation
  template_cache: true
  preload_templates: true
```

## Example Configurations

### Minimal Setup

```yaml
# .env
OPENAI_API_KEY=sk-...
```

### Enterprise Setup

```yaml
# paper-code.yaml
project:
  name: Enterprise App
  company: Acme Corp

templates:
  custom_dir: /opt/templates

ai:
  enabled: true
  model: gpt-4

ci_cd:
  provider: gitlab

validation:
  markdown:
    check_links: true
```

### Monorepo Setup

```yaml
# paper.config.json
{ "version": "1.0", "templateDir": "./corporate-templates", "projects": [...] }
```

## Configuration Priority

Settings are loaded in this order (highest priority wins):

1. Command-line flags
2. Environment variables
3. Project `paper-code.yaml`
4. User `~/.paper-code/config.yaml`
5. System `/etc/paper-code/config.yaml`
6. Built-in defaults

Example:

```bash
# CLI flag overrides everything
paper-code init --stack "Vue"  # Uses Vue, not from config

# Environment variable
PAPER_CODE_STACK=Vue paper-code init  # Uses Vue

# File configuration (lowest priority for this)
# config.yaml: stack: React  # Ignored if ENV/CLI set
```

## Validation

Validate your configuration:

```bash
paper-code config validate

# Output
✅ Configuration is valid
  - No missing required fields
  - All stacks are supported
  - All templates exist
  - OpenAI API key configured
```

## Configuration Examples

See configuration templates in:

- `examples/.env.example`
- `examples/paper.config.json`
- `examples/.paper-code/config.yaml`

## Troubleshooting

### Configuration not loading

```bash
# Check config file path
paper-code config show

# Output
Configuration sources:
1. Command line: --stack React
2. Environment: (none)
3. Project: ./paper-code.yaml
4. User: ~/.paper-code/config.yaml
5. System: /etc/paper-code/config.yaml
6. Defaults: (built-in)
```

### Invalid configuration

```bash
# Get detailed error messages
paper-code config validate --verbose
```

---

For more information, see the [CLI Usage](./cli-usage.md) guide.
