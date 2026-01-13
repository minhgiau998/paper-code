# PAPER-CODE Web GUI

A modern web interface for the PAPER-CODE project documentation generator.

## Features

- **Interactive Form**: User-friendly interface for project configuration
- **Real-time Validation**: Instant feedback on form inputs
- **AI Integration**: Optional AI-powered description generation
- **Live Preview**: See generated files before download
- **One-click Download**: Get your project as a ZIP file

## Quick Start

### Prerequisites

- Python 3.10+
- Node.js 16+ (optional, for development)

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables (optional):
```bash
# For AI features
export OPENAI_API_KEY="your-openai-api-key"
```

3. Run the server:
```bash
python main.py
```

4. Open your browser and navigate to:
```
http://localhost:8000
```

## API Endpoints

### Configuration
- `GET /api/config/project-types` - Get available project types
- `GET /api/config/tech-stacks/{project_type}` - Get tech stacks for project type
- `GET /api/config/libraries/{tech_stack}` - Get libraries for tech stack
- `GET /api/config/full` - Get complete configuration

### Generation
- `POST /api/generate` - Generate project documentation
- `GET /api/download/{project_id}` - Download generated project as ZIP

### AI
- `GET /api/ai/status` - Check AI service availability

### Utilities
- `DELETE /api/cleanup` - Clean up temporary files

## Development

### Frontend Development

The frontend is built with React and served from the `/static` directory. For development:

1. Modify files in `static/`
2. Refresh browser to see changes
3. For hot reload, consider setting up a separate React development server

### Backend Development

The backend uses FastAPI with auto-reload enabled in development mode.

## Architecture

```
web/
├── main.py              # FastAPI backend
├── requirements.txt     # Python dependencies
├── static/
│   └── index.html      # React frontend
└── README.md           # This file
```

## Security Notes

- CORS is enabled for all origins in development
- In production, restrict CORS to specific origins
- Temporary files are cleaned up automatically
- Consider adding authentication for production use

## Production Deployment

For production deployment:

1. Use a production WSGI server (Gunicorn, uWSGI)
2. Configure proper CORS settings
3. Set up reverse proxy (Nginx)
4. Enable HTTPS
5. Consider containerization (Docker)

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```
