# PAPER-CODE Documentation Templates

Reusable documentation templates for the PAPER-CODE ecosystem. Use these templates in your projects or customize them for your organization's standards.

## Installation

```bash
npm install @paper-code/templates
```

Or for yarn/pnpm:

```bash
yarn add @paper-code/templates
pnpm add @paper-code/templates
```

## Usage

### With PAPER-CODE CLI

```bash
paper-code init --template-dir ./node_modules/@paper-code/templates
```

### Custom Integration

```bash
# Copy templates to your project
cp -r node_modules/@paper-code/templates ./custom-templates

# Modify templates as needed
# Then use with paper-code
paper-code init --template-dir ./custom-templates
```

## Template Structure

```
templates/
├── core/              # Core documentation
│   ├── README.md.j2
│   ├── LICENSE.j2
│   ├── CHANGELOG.md.j2
│   └── ...
├── ai/                # AI assistant rules
│   ├── AI_RULES.md.j2
│   ├── AI_CONTEXT.md.j2
│   └── cursorrules.j2
├── stacks/            # Framework-specific docs
│   ├── frontend/
│   ├── backend/
│   └── mobile/
├── libs/              # Library-specific docs
│   ├── typescript.md.j2
│   ├── tailwindcss.md.j2
│   └── ...
└── github/            # GitHub templates
    ├── PULL_REQUEST_TEMPLATE.md.j2
    └── ci.yml.j2
```

## Available Templates

### Core Documentation

- README.md
- LICENSE (multiple options)
- CHANGELOG.md
- CONTRIBUTING.md
- SECURITY.md
- TESTING.md
- DEPLOYMENT.md

### AI & Coding Assistants

- AI_RULES.md
- AI_CONTEXT.md
- AI_WORKFLOWS.md
- cursorrules (.cursorrules for Cursor)
- copilot-instructions.md

### Frontend Frameworks

React, Vue, Angular, Next.js, Nuxt, SvelteKit, Remix, Astro

### Backend Frameworks

Express, NestJS, FastAPI, Django, Go, Ruby on Rails

### Mobile Frameworks

React Native, Flutter, Kotlin, Swift

### 100+ Libraries

TailwindCSS, Prisma, TypeScript, Redux, Docker, Kubernetes, and more

## Customization

### For Organizations

Clone and customize these templates for your company standards:

```bash
git clone https://github.com/minhgiau998/paper-code.git
cd paper-code/docs-templates
# Edit templates
npm version minor
npm publish --access public
```

### Add Custom Variables

Extend templates with organization-specific variables:

```jinja
{# In your custom template #}
{{ organization_name }}  # Your company name
{{ team_name }}          # Team identifier
{{ internal_wiki }}      # Link to wiki
```

## Contributing

Found a better template? Have improvements? Create a PR!

1. Edit templates in this directory
2. Test with PAPER-CODE CLI
3. Submit pull request

See [CONTRIBUTING.md](../docs/CONTRIBUTING.md) for details.

## License

MIT - See [LICENSE](../LICENSE)

## Support

- **Issues:** https://github.com/minhgiau998/paper-code/issues
- **Discussions:** https://github.com/minhgiau998/paper-code/discussions
- **Docs:** https://paper-code-docs.vercel.app

---

**Part of the PAPER-CODE ecosystem** 🚀
