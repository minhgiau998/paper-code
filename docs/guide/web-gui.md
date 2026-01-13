# Web GUI

Visual interface for generating documentation without the command line.

## Starting the Web Server

Start the web interface:

```bash
paper-code web
```

By default, it runs on `http://localhost:8000`

To specify a custom port:

```bash
paper-code web --port 3000
```

## Using the Web Interface

### Step 1: Configure Your Project

1. Enter your **Project Name**
2. Select **Project Type** from dropdown
3. Choose your **Tech Stack**
4. Select **Libraries & Modules** with checkboxes

### Step 2: Advanced Options

Optional settings:

- **Custom Description:** Write your project description
- **AI-Generate Description:** Use OpenAI to auto-generate
- **Template Directory:** Path to custom templates
- **Output Format:** Choose output directory structure

### Step 3: Generate

Click the **Generate Documentation** button.

The interface shows:

- Real-time progress
- Generated file list
- Download link for all files

### Step 4: Download

Download the generated documentation as a ZIP file and extract to your project.

## Features

### Live Preview

See a preview of selected options:

- Architecture recommendations
- Suggested CI/CD workflows
- Library-specific best practices

### Project Detection

Upload an existing `package.json` or `requirements.txt` to auto-detect:

- Tech stack
- Installed libraries
- Project structure

### Template Customization

Browse and select from:

- Official templates
- Community templates
- Custom organization templates

## API Endpoints

The web GUI is powered by a REST API. You can also integrate with other tools:

### Generate Documentation

```bash
POST /api/generate

{
  "name": "My Project",
  "type": "frontend",
  "stack": "React",
  "libraries": ["TypeScript", "TailwindCSS"],
  "description": "Optional project description"
}
```

### List Stacks

```bash
GET /api/stacks
```

### List Libraries

```bash
GET /api/libraries
```

### Detect Project

```bash
POST /api/detect
Content-Type: multipart/form-data

file: package.json
```

## Hosting the Web GUI

### Docker Deployment

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["paper-code", "web", "--host", "0.0.0.0"]
```

### Docker Compose

```yaml
version: "3.8"

services:
  paper-code:
    build: .
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    volumes:
      - ./output:/app/output
```

### Running Behind a Reverse Proxy

```nginx
server {
    listen 80;
    server_name docs-generator.example.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## Troubleshooting

### Port Already in Use

```bash
paper-code web --port 8001
```

### CORS Issues

The web GUI allows all origins by default. In production, restrict:

```python
# Modify allowed_origins in main.py
allowed_origins = ["https://your-domain.com"]
```

### File Download Issues

Ensure write permissions in the output directory:

```bash
chmod -R 755 ./output
```
