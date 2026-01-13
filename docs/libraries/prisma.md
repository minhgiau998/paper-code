# Prisma

Modern ORM for Node.js and TypeScript with type safety and an intuitive data model.

## Overview

Prisma is an Object-Relational Mapping (ORM) tool that provides:

- Type-safe database access
- Automated migrations
- An intuitive data model
- A web-based database explorer (Prisma Studio)

## Installation

```bash
npm install @prisma/client
npm install -D prisma
npx prisma init
```

## Schema Definition

### prisma/schema.prisma

```prisma
// Database connection
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

// Prisma client generation
generator client {
  provider = "prisma-client-js"
}

// Models
model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
  posts Post[]

  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}

model Post {
  id        Int     @id @default(autoincrement())
  title     String
  content   String?
  published Boolean @default(false)
  author    User    @relation(fields: [authorId], references: [id], onDelete: Cascade)
  authorId  Int
}
```

## Common Operations

### Create Records

```typescript
import { prisma } from "@/lib/prisma";

// Single create
const user = await prisma.user.create({
  data: {
    email: "user@example.com",
    name: "John Doe",
  },
});

// Create with relations
const post = await prisma.post.create({
  data: {
    title: "My First Post",
    content: "Content here",
    author: {
      connect: { id: user.id },
    },
  },
});
```

### Read Records

```typescript
// Find unique
const user = await prisma.user.findUnique({
  where: { email: "user@example.com" },
});

// Find first matching
const post = await prisma.post.findFirst({
  where: { published: true },
});

// Find many with filtering
const posts = await prisma.post.findMany({
  where: {
    published: true,
    author: {
      email: "user@example.com",
    },
  },
  include: { author: true },
  skip: 0,
  take: 10,
  orderBy: { createdAt: "desc" },
});

// Count records
const count = await prisma.post.count({
  where: { published: true },
});
```

### Update Records

```typescript
// Update single
const user = await prisma.user.update({
  where: { id: 1 },
  data: { name: "Jane Doe" },
});

// Update many
const result = await prisma.post.updateMany({
  where: { published: false },
  data: { published: true },
});
```

### Delete Records

```typescript
// Delete single
await prisma.post.delete({
  where: { id: 1 },
});

// Delete many
await prisma.post.deleteMany({
  where: {
    published: false,
    createdAt: {
      lt: new Date("2023-01-01"),
    },
  },
});
```

## Relations

### One-to-Many

```prisma
model Author {
  id    Int     @id @default(autoincrement())
  posts Post[]
}

model Post {
  id       Int @id @default(autoincrement())
  author   Author @relation(fields: [authorId], references: [id])
  authorId Int
}
```

### Many-to-Many

```prisma
model Post {
  id    Int      @id @default(autoincrement())
  tags  Tag[]
}

model Tag {
  id    Int      @id @default(autoincrement())
  posts Post[]
}
```

### Self-Relations

```prisma
model Comment {
  id       Int       @id @default(autoincrement())
  text     String
  replies  Comment[] @relation("CommentReplies")
  parent   Comment?  @relation("CommentReplies", fields: [parentId], references: [id])
  parentId Int?
}
```

## Advanced Queries

### Raw SQL

```typescript
const users = await prisma.$queryRaw`
  SELECT * FROM User WHERE email = ${email}
`;
```

### Transactions

```typescript
const [user, post] = await prisma.$transaction([
  prisma.user.create({ data: userData }),
  prisma.post.create({ data: postData }),
]);
```

### Aggregations

```typescript
const stats = await prisma.post.aggregate({
  _count: true,
  _avg: { viewCount: true },
  _max: { viewCount: true },
  where: { published: true },
});
```

## Migrations

### Create Migration

```bash
# Create migration files
npx prisma migrate dev --name add_post_model

# Deploy to production
npx prisma migrate deploy
```

### Schema Introspection

```bash
# Generate Prisma schema from existing database
npx prisma db pull
```

## Prisma Studio

```bash
# Open web UI to explore database
npx prisma studio
```

## Best Practices

### 1. Use Type Safety

```typescript
// ✅ Good - Type-safe
type UserInput = Prisma.UserCreateInput;
async function createUser(data: UserInput) {
  return prisma.user.create({ data });
}

// ❌ Avoid - Not type-safe
async function createUser(data: any) {
  return prisma.user.create({ data });
}
```

### 2. Lazy Load Relations

```typescript
// ✅ Load relations only when needed
const posts = await prisma.post.findMany({
  include: { author: true }, // Only when needed
});

// ❌ Avoid - N+1 queries
const posts = await prisma.post.findMany();
const postsWithAuthors = await Promise.all(
  posts.map((post) => prisma.user.findUnique({ where: { id: post.authorId } }))
);
```

### 3. Use Select for Performance

```typescript
// ✅ Select only needed fields
const posts = await prisma.post.findMany({
  select: {
    id: true,
    title: true,
    author: {
      select: { name: true },
    },
  },
});
```

### 4. Reuse Prisma Client

```typescript
// lib/prisma.ts
import { PrismaClient } from "@prisma/client";

const globalForPrisma = globalThis as unknown as { prisma: PrismaClient };
export const prisma = globalForPrisma.prisma || new PrismaClient();

if (process.env.NODE_ENV !== "production") {
  globalForPrisma.prisma = prisma;
}
```

## Resources

- **Documentation**: https://www.prisma.io/docs
- **API Reference**: https://www.prisma.io/docs/reference/api-reference/prisma-client-reference
- **Community**: https://discord.com/invite/KQyTW2H2rJ
