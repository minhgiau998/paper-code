# PAPER-CODE Documentation

Official documentation site for PAPER-CODE, built with VitePress.

## Local Development

### Install Dependencies

```bash
npm install
```

### Start Development Server

```bash
npm run docs:dev
```

The site will be available at `http://localhost:5173`

### Build for Production

```bash
npm run docs:build
```

Output will be in `.vitepress/dist/`

### Preview Production Build

```bash
npm run docs:preview
```

## Structure

```
docs/
├── .vitepress/
│   ├── config.ts          # VitePress configuration
│   └── theme/
│       ├── index.ts       # Theme customization
│       └── style.css      # Global styles
├── index.md               # Home page
├── features.md            # Features page
├── architecture.md        # Architecture guide
├── api-reference.md       # API documentation
├── guide/                 # User guides
│   ├── installation.md
│   ├── quick-start.md
│   ├── cli-usage.md
│   ├── web-gui.md
│   ├── project-types.md
│   ├── ai-generation.md
│   └── custom-templates.md
├── stacks/                # Tech stack documentation
│   ├── index.md
│   ├── frontend/
│   ├── backend/
│   └── mobile/
├── libraries/             # Library documentation
│   ├── index.md
│   ├── tailwindcss.md
│   ├── prisma.md
│   └── ...
└── package.json           # Dependencies
```

## Writing Documentation

### Page Format

```markdown
# Page Title

## Section Heading

Content with **bold** and _italic_ text.

### Code Example

\`\`\`typescript
const example = "code";
\`\`\`

### Tables

| Column 1 | Column 2 |
| -------- | -------- |
| Value 1  | Value 2  |
```

### Front Matter

Optional configuration at the top of pages:

```yaml
---
title: Custom Title
description: Page description
---
```

### Navigation Sidebar

Configured in `.vitepress/config.ts` under `themeConfig.sidebar`

## Deployment

### Vercel (Recommended)

```bash
# Push to GitHub
git push

# Vercel automatically deploys from main branch
# Build command: npm run docs:build
# Output directory: docs/.vitepress/dist
```

### GitHub Pages

```bash
# Configure in .vitepress/config.ts
export default {
  base: '/paper-code/',  // If in subdirectory
  ...
}

# Deploy
npm run docs:build
# Push dist folder to gh-pages branch
```

### Docker

```dockerfile
FROM node:18-alpine

WORKDIR /app
COPY docs/ .
RUN npm install && npm run docs:build

FROM nginx:alpine
COPY --from=0 /app/.vitepress/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

## Contributing

When adding new documentation:

1. **Create Markdown file** in appropriate folder
2. **Update sidebar configuration** in `config.ts`
3. **Use consistent formatting** with existing pages
4. **Test locally** with `npm run docs:dev`
5. **Include code examples** where relevant

## Content Guidelines

- **Clarity**: Write for beginners and experts
- **Brevity**: Keep sections focused and concise
- **Examples**: Include practical code examples
- **Links**: Cross-reference related topics
- **Images**: Add diagrams using Mermaid or ASCII art

## Search

VitePress provides built-in local search. Configure in `config.ts`:

```typescript
search: {
  provider: "local";
}
```

## Analytics

To add analytics (optional):

```typescript
// .vitepress/config.ts
export default {
  head: [
    ["script", { async: "", src: "https://www.googletagmanager.com/gtag/..." }],
  ],
};
```

## Troubleshooting

### Port already in use

```bash
npm run docs:dev -- --port 5174
```

### Build fails

```bash
# Clear cache
rm -rf .vitepress/.cache
npm run docs:build
```

### Changes not showing

```bash
# Hard refresh
Ctrl+Shift+R (Windows/Linux) or Cmd+Shift+R (Mac)
```

## Resources

- [VitePress Documentation](https://vitepress.dev)
- [Markdown Guide](https://www.markdownguide.org)
- [Mermaid Diagrams](https://mermaid.js.org)

---

Built with ❤️ for the PAPER-CODE community
