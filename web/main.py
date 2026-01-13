"""
PAPER-CODE Web GUI - FastAPI Backend
Provides REST API for project documentation generation
"""

import os
import sys
import json
import tempfile
import shutil
from pathlib import Path
from typing import Dict, Any, List, Optional
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel

# Add src directory to path to import paper-code modules
sys.path.append(str(Path(__file__).parent.parent / "src"))

from config import PROJECT_TYPES, TECH_STACKS, LIBRARIES
from generator import DocGenerator
from ai_service import AIService

# Temporary storage for generated projects
TEMP_DIR = Path(tempfile.gettempdir()) / "paper-code-web"

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Create temporary directory on startup"""
    TEMP_DIR.mkdir(exist_ok=True)
    yield
    # Cleanup on shutdown (optional)
    # if TEMP_DIR.exists():
    #     shutil.rmtree(TEMP_DIR)

# Initialize FastAPI app
app = FastAPI(
    title="PAPER-CODE Web GUI",
    description="Interactive Project Documentation Generator - Web Interface",
    version="1.0.0",
    lifespan=lifespan
)

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for request/response
class ProjectConfig(BaseModel):
    project_name: str
    description: str
    project_type: str
    tech_stack: str
    libraries: List[str]
    ai_generate: bool = False
    ai_hint: Optional[str] = None
    template_dir: Optional[str] = None
    update_mode: bool = False

class GenerationRequest(BaseModel):
    config: ProjectConfig
    output_dir: Optional[str] = None

class GenerationResponse(BaseModel):
    success: bool
    message: str
    output_path: Optional[str] = None
    files_generated: Optional[List[str]] = None

# Get the directory where this script is located
BASE_DIR = Path(__file__).parent
STATIC_DIR = BASE_DIR / "static"

# Mount static files
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

@app.get("/")
async def root():
    """Root endpoint - serves frontend"""
    static_path = STATIC_DIR / "index.html"
    return FileResponse(str(static_path))

@app.get("/api/config/project-types")
async def get_project_types():
    """Get available project types"""
    return {"project_types": PROJECT_TYPES}

@app.get("/api/config/tech-stacks/{project_type}")
async def get_tech_stacks(project_type: str):
    """Get available tech stacks for a project type"""
    stacks = TECH_STACKS.get(project_type, [])
    return {"tech_stacks": stacks}

@app.get("/api/config/libraries/{tech_stack}")
async def get_libraries(tech_stack: str):
    """Get available libraries for a tech stack"""
    libraries = LIBRARIES.get(tech_stack, [])
    return {"libraries": libraries}

@app.get("/api/config/full")
async def get_full_config():
    """Get complete configuration structure"""
    return {
        "project_types": PROJECT_TYPES,
        "tech_stacks": TECH_STACKS,
        "libraries": LIBRARIES
    }

@app.post("/api/generate")
async def generate_project(request: GenerationRequest, background_tasks: BackgroundTasks):
    """Generate project documentation"""
    try:
        # Create temporary output directory
        output_dir = TEMP_DIR / f"project_{hash(str(request.config)) % 1000000}"
        output_dir.mkdir(exist_ok=True)
        
        # Convert Pydantic model to dict for generator
        config_dict = request.config.dict()
        
        # Initialize AI service if requested
        if request.config.ai_generate:
            ai_service = AIService()
            if ai_service.is_available():
                # Generate AI description
                ai_description = ai_service.generate_project_description(
                    project_name=config_dict["project_name"],
                    project_type=config_dict["project_type"],
                    tech_stack=config_dict["tech_stack"],
                    libraries=config_dict["libraries"],
                    user_hint=config_dict.get("ai_hint", "")
                )
                config_dict["description"] = ai_description
            else:
                raise HTTPException(
                    status_code=400, 
                    detail="AI service not available. Set OPENAI_API_KEY environment variable."
                )
        
        # Generate documentation
        generator = DocGenerator(
            str(output_dir), 
            config_dict.get("template_dir"), 
            config_dict.get("update_mode", False)
        )
        generator.generate_project(config_dict)
        
        # List generated files
        generated_files = []
        for root, dirs, files in os.walk(output_dir):
            for file in files:
                file_path = Path(root) / file
                relative_path = file_path.relative_to(output_dir)
                generated_files.append(str(relative_path))
        
        return GenerationResponse(
            success=True,
            message="Project documentation generated successfully!",
            output_path=str(output_dir),
            files_generated=generated_files
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/download/{project_id}")
async def download_project(project_id: str):
    """Download generated project as ZIP file"""
    try:
        project_dir = TEMP_DIR / f"project_{project_id}"
        if not project_dir.exists():
            raise HTTPException(status_code=404, detail="Project not found")
        
        # Create ZIP file
        zip_path = TEMP_DIR / f"project_{project_id}.zip"
        shutil.make_archive(str(zip_path.with_suffix("")), "zip", project_dir)
        
        return FileResponse(
            zip_path,
            media_type="application/zip",
            filename=f"paper-code-project-{project_id}.zip"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/ai/status")
async def get_ai_status():
    """Check if AI service is available"""
    ai_service = AIService()
    return {"available": ai_service.is_available()}

@app.delete("/api/cleanup")
async def cleanup_temp_files():
    """Clean up temporary files"""
    try:
        if TEMP_DIR.exists():
            shutil.rmtree(TEMP_DIR)
            TEMP_DIR.mkdir(exist_ok=True)
        return {"message": "Temporary files cleaned up successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
