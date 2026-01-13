# Documentation Site

This directory contains the official VitePress-based documentation site for PAPER-CODE.

## Quick Links

- **Home**: [index.md](index.md)
- **Installation**: [guide/installation.md](guide/installation.md)
- **Quick Start**: [guide/quick-start.md](guide/quick-start.md)
- **Tech Stacks**: [stacks/](stacks/)
- **Libraries**: [libraries/](libraries/)
- **API Reference**: [api-reference.md](api-reference.md)

## Local Development

```bash
# Install dependencies
npm install

# Start dev server
npm run docs:dev

# Build for production
npm run docs:build

# Preview production build
npm run docs:preview
```

## Adding Documentation

### New Guide Page

Create in `guide/` directory:

```markdown
# Topic Name

Introduction paragraph.

## Section 1

Content here.

## Section 2

Content here.
```

Then add to sidebar in [`.vitepress/config.ts`](.vitepress/config.ts).

### New Tech Stack

Create in `stacks/frontend/` (or backend/mobile/):

```markdown
# Tech Stack Name

## Overview

...

## Project Structure

...
```

### New Library

Create in `libraries/`:

```markdown
# Library Name

## Installation

...

## Usage

...
```

## File Structure

```
docs/
├── .vitepress/          # VitePress config and theme
├── guide/               # User guides (12 pages)
├── stacks/              # Tech stack docs
├── libraries/           # Library documentation
├── features.md          # Features overview
├── architecture.md      # Architecture guide
├── api-reference.md     # REST API docs
├── index.md             # Home page
└── package.json         # Dependencies
```

## Sidebar Configuration

Edit `.vitepress/config.ts` to update navigation:

```typescript
sidebar: {
  '/guide/': [
    {
      text: 'Getting Started',
      items: [
        { text: 'Installation', link: '/guide/installation' },
        ...
      ]
    }
  ]
}
```

## Deployment

### Vercel (Recommended)

1. Push to GitHub
2. Connect repo to Vercel
3. Build command: `npm run docs:build`
4. Output dir: `docs/.vitepress/dist`

### GitHub Pages

```bash
# Update base in config.ts if needed
# base: '/paper-code/'

npm run docs:build
# Push .vitepress/dist to gh-pages branch
```

### Docker

See deployment section in [README.md](README.md).

## Contributing

- Write in Markdown
- Follow existing style
- Include code examples
- Test locally first
- Keep pages focused

## Resources

- [VitePress Docs](https://vitepress.dev)
- [Markdown Guide](https://www.markdownguide.org)
- [Paper-Code GitHub](https://github.com/minhgiau998/paper-code)
