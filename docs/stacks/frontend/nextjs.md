# Next.js

Full-stack React framework with server-side rendering, static generation, and built-in API routes.

## Overview

Next.js extends React with server-side capabilities, making it ideal for production applications that need SEO, performance, and scalability out of the box.

## Key Features

- **Server-Side Rendering (SSR)**: Generate HTML on the server for each request
- **Static Site Generation (SSG)**: Pre-render pages at build time
- **Incremental Static Regeneration (ISR)**: Re-validate and regenerate pages
- **API Routes**: Build backend endpoints in the same project
- **Image Optimization**: Automatic image optimization and loading
- **Built-in Routing**: File-based routing system

## Project Structure

```
my-app/
├── app/                    # App Router (Next.js 13+)
│   ├── page.tsx            # Home page
│   ├── layout.tsx          # Root layout
│   ├── blog/
│   │   ├── page.tsx        # /blog page
│   │   ├── [slug]/         # Dynamic route /blog/[slug]
│   │   │   └── page.tsx
│   │   └── layout.tsx      # Shared blog layout
│   └── api/
│       ├── posts/          # /api/posts endpoint
│       │   ├── route.ts    # GET, POST handlers
│       │   └── [id]/
│       │       └── route.ts
│       └── auth/
│           └── [...nextauth]/
│               └── route.ts
├── public/                 # Static files
├── styles/                 # Global styles
├── lib/                    # Utility functions
├── components/             # Reusable components
└── next.config.ts          # Next.js configuration
```

## Rendering Strategies

### Server-Side Rendering (SSR)

```typescript
// app/page.tsx - Re-rendered on each request
export default async function Page() {
  const data = await fetch("https://api.example.com/data", {
    cache: "no-store", // Don't cache
  });
  return <div>{data}</div>;
}
```

### Static Site Generation (SSG)

```typescript
// Pre-rendered at build time
export default function Post({ post }: Props) {
  return <article>{post.content}</article>;
}

export async function generateStaticParams() {
  const posts = await fetch("https://api.example.com/posts").then((r) =>
    r.json()
  );
  return posts.map((post) => ({ slug: post.slug }));
}
```

### Incremental Static Regeneration

```typescript
// Re-validate every 60 seconds
export const revalidate = 60;

export default async function Page() {
  const data = await fetch("https://api.example.com/data");
  return <div>{data}</div>;
}
```

## API Routes

```typescript
// app/api/posts/route.ts
import { NextRequest, NextResponse } from "next/server";

export async function GET(request: NextRequest) {
  const posts = await db.posts.findMany();
  return NextResponse.json(posts);
}

export async function POST(request: NextRequest) {
  const body = await request.json();
  const post = await db.posts.create(body);
  return NextResponse.json(post, { status: 201 });
}
```

## Common Libraries Integration

### Database (Prisma)

```typescript
// lib/prisma.ts
import { PrismaClient } from "@prisma/client";

const globalForPrisma = globalThis as unknown as { prisma: PrismaClient };
export const prisma = globalForPrisma.prisma || new PrismaClient();

if (process.env.NODE_ENV !== "production") globalForPrisma.prisma = prisma;
```

### Authentication (NextAuth.js)

```typescript
// app/api/auth/[...nextauth]/route.ts
import NextAuth from "next-auth";
import Credentials from "next-auth/providers/credentials";

export const { handlers, auth, signIn, signOut } = NextAuth({
  providers: [
    Credentials({
      async authorize(credentials) {
        const user = await db.user.findUnique({
          where: { email: credentials.email },
        });
        return user;
      },
    }),
  ],
});
```

### Environment Configuration

```typescript
// lib/config.ts
const config = {
  isDevelopment: process.env.NODE_ENV === "development",
  isProduction: process.env.NODE_ENV === "production",
  apiUrl: process.env.NEXT_PUBLIC_API_URL || "http://localhost:3000",
};

export default config;
```

## Middleware

```typescript
// middleware.ts
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function middleware(request: NextRequest) {
  // Add custom headers
  const requestHeaders = new Headers(request.headers);
  requestHeaders.set("x-pathname", request.nextUrl.pathname);

  return NextResponse.next({
    request: {
      headers: requestHeaders,
    },
  });
}

export const config = {
  matcher: ["/api/:path*", "/dashboard/:path*"],
};
```

## Testing

```typescript
// __tests__/api.test.ts
import { GET } from "@/app/api/posts/route";

describe("POST /api/posts", () => {
  it("returns list of posts", async () => {
    const response = await GET(new Request("http://localhost:3000"));
    const data = await response.json();
    expect(data).toBeInstanceOf(Array);
  });
});
```

## Performance Tips

1. **Image Optimization**: Use `next/image`
2. **Font Optimization**: Use `next/font`
3. **Code Splitting**: Automatic per-route
4. **Tree Shaking**: Remove unused code
5. **Bundle Analysis**: `npm run build -- --analyze`

## Deployment

### Vercel (Recommended)

```bash
# Deploy automatically from GitHub
# 1. Push to GitHub
# 2. Connect repo on Vercel
# 3. Environment variables auto-configured
```

### Docker

```dockerfile
FROM node:18-alpine AS builder
WORKDIR /app
COPY . .
RUN npm ci && npm run build

FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/.next ./.next
COPY package*.json .
RUN npm ci --only=production
EXPOSE 3000
CMD ["npm", "start"]
```

## Resources

- **Documentation**: https://nextjs.org/docs
- **Vercel Deployment**: https://vercel.com/docs
- **App Router Guide**: https://nextjs.org/docs/app
