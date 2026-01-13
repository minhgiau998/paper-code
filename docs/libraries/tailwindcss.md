# TailwindCSS

Utility-first CSS framework for rapidly building custom designs.

## Overview

TailwindCSS is a utility-first CSS framework that helps you build modern designs without leaving your HTML. Instead of writing custom CSS, you compose pre-made utility classes.

## Installation

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

## Configuration

### tailwind.config.js

```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#3b82f6",
        secondary: "#10b981",
      },
      spacing: {
        128: "32rem",
        144: "36rem",
      },
    },
  },
  plugins: [],
};
```

## Common Utilities

### Layout & Display

```html
<!-- Flexbox -->
<div class="flex gap-4">
  <div class="flex-1">Content</div>
</div>

<!-- Grid -->
<div class="grid grid-cols-3 gap-4">
  <div>Item 1</div>
</div>

<!-- Positioning -->
<div class="relative">
  <div class="absolute inset-0">Overlay</div>
</div>
```

### Spacing

```html
<!-- Padding -->
<div class="p-4 px-6 py-2">Content</div>

<!-- Margin -->
<div class="mt-4 mb-2 mx-auto">Content</div>

<!-- Gap (flexbox/grid) -->
<div class="flex gap-4">Content</div>
```

### Typography

```html
<!-- Font Size & Weight -->
<h1 class="text-4xl font-bold">Heading</h1>
<p class="text-base font-normal">Paragraph</p>

<!-- Text Color & Alignment -->
<p class="text-gray-700 text-center">Centered text</p>
```

### Colors

```html
<!-- Background -->
<div class="bg-blue-500">Content</div>
<div class="bg-gradient-to-r from-blue-500 to-purple-600">Gradient</div>

<!-- Text -->
<p class="text-red-500">Red text</p>

<!-- Borders -->
<div class="border-2 border-blue-500">Content</div>
```

### Responsive Design

```html
<!-- Mobile-first -->
<div class="text-sm md:text-base lg:text-lg">Responsive text</div>

<!-- Hide/Show based on breakpoint -->
<div class="hidden lg:block">Visible on large screens</div>

<!-- Full grid layout example -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
  <div>Item 1</div>
</div>
```

## Common Patterns

### Button Component

```typescript
// components/Button.tsx
interface ButtonProps {
  variant?: "primary" | "secondary" | "outline";
  size?: "sm" | "md" | "lg";
  children: React.ReactNode;
}

export function Button({
  variant = "primary",
  size = "md",
  children,
}: ButtonProps) {
  const variants = {
    primary: "bg-blue-500 text-white hover:bg-blue-600",
    secondary: "bg-gray-500 text-white hover:bg-gray-600",
    outline: "border-2 border-blue-500 text-blue-500 hover:bg-blue-50",
  };

  const sizes = {
    sm: "px-2 py-1 text-sm",
    md: "px-4 py-2 text-base",
    lg: "px-6 py-3 text-lg",
  };

  return (
    <button
      className={`${variants[variant]} ${sizes[size]} rounded transition`}
    >
      {children}
    </button>
  );
}
```

### Card Component

```typescript
export function Card({ title, children }: Props) {
  return (
    <div class="bg-white rounded-lg shadow-md p-6">
      {title && <h3 class="text-lg font-semibold mb-4">{title}</h3>}
      {children}
    </div>
  );
}
```

### Form Input

```typescript
export function Input({ label, ...props }: Props) {
  return (
    <div class="mb-4">
      {label && <label class="block text-sm font-medium mb-2">{label}</label>}
      <input
        class="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
        {...props}
      />
    </div>
  );
}
```

## Advanced Features

### Custom Utilities

```javascript
// tailwind.config.js
module.exports = {
  plugins: [
    function ({ addUtilities }) {
      addUtilities({
        ".text-shadow": {
          textShadow: "2px 2px 4px rgba(0, 0, 0, 0.1)",
        },
        ".center": {
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        },
      });
    },
  ],
};
```

### Custom Variants

```javascript
module.exports = {
  plugins: [
    function ({ addVariant }) {
      addVariant("supports-grid", "@supports (display: grid)");
    },
  ],
};
```

## Best Practices

1. **Use Tailwind with Components**: Combine with component frameworks
2. **Extract Repeated Patterns**: Use `@apply` for complex utilities
3. **Customize Thoughtfully**: Only extend what you need
4. **Responsive Mobile-First**: Design for mobile, enhance for larger screens
5. **Dark Mode**: Built-in dark mode support

### Using @apply

```css
/* input.css */
@layer components {
  .btn-primary {
    @apply px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition;
  }
}
```

## Performance

- **Tree-shaking**: Tailwind removes unused CSS in production
- **Production Build**: Typically 5-15KB gzipped
- **PurgeCSS**: Configured in `content` array

## Plugins

Popular TailwindCSS plugins:

- **@tailwindcss/forms** - Styled form elements
- **@tailwindcss/typography** - Prose styling
- **@tailwindcss/container-queries** - Container queries support

```bash
npm install -D @tailwindcss/forms
```

```javascript
// tailwind.config.js
module.exports = {
  plugins: [require("@tailwindcss/forms")],
};
```

## Resources

- **Documentation**: https://tailwindcss.com
- **Component Library**: https://ui.shadcn.com
- **Tailwind UI**: https://tailwindui.com
- **Tailwind CSS Intellisense**: VS Code extension
