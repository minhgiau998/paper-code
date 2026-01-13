# API Reference

Complete API reference for PAPER-CODE's REST endpoints.

## Base URL

```
http://localhost:8000/api
```

## Authentication

Currently, no authentication is required. In production, add authentication headers as needed.

## Generate Documentation

Generate project documentation from a configuration.

### Request

```http
POST /api/generate
Content-Type: application/json

{
  "name": "My Project",
  "type": "frontend",
  "stack": "React",
  "libraries": ["TypeScript", "TailwindCSS"],
  "description": "Optional project description"
}
```

### Parameters

| Parameter     | Type    | Required | Description                                    |
| ------------- | ------- | -------- | ---------------------------------------------- |
| `name`        | string  | Yes      | Project name                                   |
| `type`        | string  | Yes      | Project type (frontend, backend, mobile, etc.) |
| `stack`       | string  | Yes      | Tech stack (React, Next.js, NestJS, etc.)      |
| `libraries`   | array   | No       | Selected libraries and tools                   |
| `description` | string  | No       | Project description                            |
| `templateDir` | string  | No       | Custom template directory path                 |
| `aiGenerate`  | boolean | No       | Use AI to generate description                 |

### Response

```http
HTTP/1.1 200 OK
Content-Type: application/zip

[Binary ZIP file containing generated documentation]
```

### Example cURL

```bash
curl -X POST http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My App",
    "type": "frontend",
    "stack": "React",
    "libraries": ["TypeScript", "TailwindCSS"]
  }' \
  -o docs.zip
```

### Example JavaScript

```javascript
const response = await fetch("http://localhost:8000/api/generate", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    name: "My App",
    type: "frontend",
    stack: "React",
    libraries: ["TypeScript", "TailwindCSS"],
  }),
});

const blob = await response.blob();
const url = URL.createObjectURL(blob);
const a = document.createElement("a");
a.href = url;
a.download = "docs.zip";
a.click();
```

## List Stacks

Get available tech stacks grouped by category.

### Request

```http
GET /api/stacks
```

### Response

```json
{
  "frontend": ["React", "Vue", "Angular", "Next.js", "Nuxt", "SvelteKit"],
  "backend": ["Express", "NestJS", "FastAPI", "Django", "Go"],
  "mobile": ["React Native", "Flutter", "Kotlin", "Swift"]
}
```

### Example

```bash
curl http://localhost:8000/api/stacks | jq .
```

## List Libraries

Get available libraries grouped by category.

### Request

```http
GET /api/libraries
```

### Response

```json
{
  "state-management": ["Redux Toolkit", "Zustand", "Jotai", "Pinia"],
  "data-fetching": ["TanStack Query", "Axios", "SWR"],
  "ui-frameworks": ["shadcn/ui", "Material UI", "Chakra UI"],
  "styling": ["TailwindCSS", "CSS Modules", "Emotion"]
}
```

## Detect Project

Auto-detect project stack and libraries from uploaded file.

### Request

```http
POST /api/detect
Content-Type: multipart/form-data

file: @package.json
```

### Response

```json
{
  "detectedStack": "React",
  "detectedType": "frontend",
  "libraries": ["TypeScript", "React", "React DOM"],
  "confidence": 0.95
}
```

### Example

```bash
curl -F "file=@package.json" http://localhost:8000/api/detect | jq .
```

## Get Stack Details

Get detailed information about a specific stack.

### Request

```http
GET /api/stacks/{stackName}
```

### Response

```json
{
  "name": "React",
  "category": "frontend",
  "description": "JavaScript library for building UIs",
  "libraries": ["TypeScript", "TailwindCSS", "Redux"],
  "architectureTemplate": "react_arch.md",
  "standardsTemplate": "react_standards.md"
}
```

## Get Library Details

Get detailed information about a specific library.

### Request

```http
GET /api/libraries/{libraryName}
```

### Response

```json
{
  "name": "TailwindCSS",
  "category": "styling",
  "description": "Utility-first CSS framework",
  "documentation": "https://tailwindcss.com",
  "compatibleStacks": ["React", "Vue", "Angular", "Next.js"],
  "documentationTemplate": "tailwindcss.md"
}
```

## Error Responses

### 400 Bad Request

Invalid request parameters.

```json
{
  "error": "Bad Request",
  "message": "Stack 'InvalidStack' not supported",
  "details": {
    "availableStacks": ["React", "Vue", "Angular"]
  }
}
```

### 422 Unprocessable Entity

Validation error.

```json
{
  "error": "Validation Error",
  "message": "Missing required field: 'type'",
  "fields": {
    "type": "This field is required"
  }
}
```

### 500 Internal Server Error

Server error during generation.

```json
{
  "error": "Internal Server Error",
  "message": "Failed to render templates",
  "details": "Template not found: stacks/frontend/react_arch.md.j2"
}
```

## Rate Limiting

Currently no rate limiting is enforced. In production, implement appropriate limits.

## CORS

CORS is enabled for all origins in development. In production, restrict to specific origins:

```python
# web/main.py
allowed_origins = ["https://your-domain.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Webhooks

Webhooks can be configured to notify external systems when documentation is generated:

```python
@app.post("/api/webhooks")
async def register_webhook(webhook: WebhookConfig):
    # Register webhook
    # Call webhook after generation
    pass
```

## Batch Operations

For generating multiple projects at once, use the CLI batch mode instead of repeated API calls:

```bash
paper-code generate --config projects.json
```

## Changelog

### API v1.0.0

- Initial release with core endpoints
- Generate, list stacks, list libraries
- File upload for project detection

---

For more information, see the [Web GUI documentation](../guide/web-gui.md) or [CLI Usage guide](../guide/cli-usage.md).
