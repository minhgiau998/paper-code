# React

Modern, component-based UI library by Facebook for building interactive user interfaces.

## Overview

React is a JavaScript library for building user interfaces with reusable components. It uses a declarative approach where you describe what the UI should look like, and React handles the rendering.

## Key Characteristics

- **Component-Based**: Build encapsulated components that manage their own state
- **Virtual DOM**: Efficient rendering and reconciliation
- **Unidirectional Data Flow**: Predictable state management
- **Large Ecosystem**: Extensive third-party library support
- **Strong Community**: Largest React community and resources

## Architecture Overview

### Component Hierarchy

```
App (Root)
├── Header
│   ├── Logo
│   └── Navigation
├── MainContent
│   ├── Sidebar
│   └── ContentArea
│       ├── BlogPost
│       └── Comments
└── Footer
```

### State Management Patterns

```
┌─────────────────────────────────────────────┐
│           Application State                 │
├─────────────────────────────────────────────┤
│                                             │
│  Global: Redux / Zustand / Recoil          │
│  ├── User Authentication                   │
│  ├── App Settings                          │
│  └── Theme Preferences                     │
│                                             │
│  Server: TanStack Query / SWR              │
│  ├── API Data                              │
│  ├── Cache Management                      │
│  └── Synchronization                       │
│                                             │
│  Local: useState / useReducer              │
│  ├── Form Inputs                           │
│  ├── UI Toggle States                      │
│  └── Temporary Data                        │
└─────────────────────────────────────────────┘
```

## Project Structure

```
src/
├── components/           # Shared components
│   ├── ui/              # Primitive UI components (Button, Input)
│   └── layout/          # Layout components (Header, Sidebar)
├── features/            # Feature modules (domain-driven)
│   ├── auth/
│   │   ├── api/         # Auth API calls
│   │   ├── components/  # Auth-specific components
│   │   ├── hooks/       # Auth hooks (useAuth)
│   │   └── store/       # Auth state
│   ├── dashboard/
│   └── posts/
├── hooks/               # Global custom hooks
├── store/               # Global state management (Redux, Zustand)
├── services/            # API and external services
├── utils/               # Utility functions
├── types/               # TypeScript types
├── styles/              # Global styles
└── App.tsx              # Root component
```

## Common Libraries

| Category         | Recommended                  | Alternative            |
| ---------------- | ---------------------------- | ---------------------- |
| **Routing**      | React Router v6              | TanStack Router        |
| **State**        | Redux Toolkit / Zustand      | Jotai, Recoil          |
| **Server State** | TanStack Query               | SWR                    |
| **UI Framework** | shadcn/ui                    | Material UI, Chakra UI |
| **Styling**      | TailwindCSS                  | CSS Modules, Emotion   |
| **Forms**        | React Hook Form              | Formik                 |
| **Validation**   | Zod / TypeScript             | Yup                    |
| **Testing**      | Jest + React Testing Library | Vitest + Playwright    |

## Coding Standards

### Component Naming

```typescript
// ✅ Good - PascalCase
export function UserCard({ userId }: Props) {
  return <div>{userId}</div>;
}

// ❌ Avoid - camelCase
export function userCard({ userId }: Props) {
  return <div>{userId}</div>;
}
```

### Props Definition

```typescript
// ✅ Good - typed props
interface UserCardProps {
  userId: string;
  onDelete: (id: string) => void;
  isActive?: boolean;
}

export function UserCard({ userId, onDelete, isActive }: UserCardProps) {
  // ...
}

// ❌ Avoid - any type
export function UserCard(props: any) {
  // ...
}
```

### Hooks Usage

```typescript
// ✅ Good - use custom hooks to manage state
function useUserData(userId: string) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true);
    fetchUser(userId)
      .then(setUser)
      .finally(() => setLoading(false));
  }, [userId]);

  return { user, loading };
}

// Use in component
export function UserProfile({ userId }: Props) {
  const { user, loading } = useUserData(userId);

  if (loading) return <div>Loading...</div>;
  return <div>{user?.name}</div>;
}
```

## Performance Optimization

### Memoization

```typescript
// Prevent unnecessary re-renders
export const UserCard = memo(({ user }: Props) => <div>{user.name}</div>);

// Or with custom comparison
export const UserCard = memo(
  ({ user }: Props) => <div>{user.name}</div>,
  (prev, next) => prev.user.id === next.user.id
);
```

### Code Splitting

```typescript
import { lazy, Suspense } from "react";

const Dashboard = lazy(() => import("./Dashboard"));

export function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <Dashboard />
    </Suspense>
  );
}
```

## Testing

### Component Testing

```typescript
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { UserCard } from "./UserCard";

describe("UserCard", () => {
  it("renders user information", () => {
    render(<UserCard userId="123" />);
    expect(screen.getByText("User")).toBeInTheDocument();
  });

  it("calls onDelete when delete button is clicked", async () => {
    const handleDelete = jest.fn();
    render(<UserCard userId="123" onDelete={handleDelete} />);

    await userEvent.click(screen.getByRole("button", { name: /delete/i }));
    expect(handleDelete).toHaveBeenCalledWith("123");
  });
});
```

## Deployment

### Build Optimization

```bash
# Create optimized production build
npm run build

# Analyze bundle size
npm run build -- --analyze
```

### Environment Configuration

```typescript
// config/env.ts
const config = {
  development: {
    apiUrl: "http://localhost:3000",
    debug: true,
  },
  production: {
    apiUrl: "https://api.example.com",
    debug: false,
  },
};

export default config[process.env.NODE_ENV || "development"];
```

## Security Best Practices

1. **Sanitize User Input**: Always sanitize data displayed in the DOM
2. **CSRF Protection**: Use tokens for state-changing requests
3. **XSS Prevention**: Never use `dangerouslySetInnerHTML` with user content
4. **Environment Variables**: Store secrets in environment variables only

```typescript
// ✅ Good - React auto-escapes by default
<div>{userInput}</div>

// ❌ Avoid - XSS vulnerability
<div dangerouslySetInnerHTML={{ __html: userInput }} />
```

## Common Patterns

### Custom Hooks

```typescript
function useFetch<T>(url: string) {
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    fetch(url)
      .then((res) => res.json())
      .then(setData)
      .catch(setError);
  }, [url]);

  return { data, error };
}
```

### Error Boundary

```typescript
export class ErrorBoundary extends React.Component<Props, State> {
  componentDidCatch(error: Error) {
    this.setState({ hasError: true, error });
  }

  render() {
    if (this.state.hasError) {
      return <div>Error: {this.state.error?.message}</div>;
    }
    return this.props.children;
  }
}
```

## Resources

- **Official Documentation**: https://react.dev
- **React Router**: https://reactrouter.com
- **TanStack Query**: https://tanstack.com/query
- **React Testing Library**: https://testing-library.com/react
