#!/usr/bin/env python3
"""
PAPER-CODE Web GUI Startup Script
Quick launcher for the web interface
"""

import os
import sys
import subprocess
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    required_packages = ['fastapi', 'uvicorn', 'jinja2', 'python-dotenv', 'aiofiles']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n📦 Install with: pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies satisfied")
    return True

def check_src_module():
    """Check if src module is accessible"""
    src_path = Path(__file__).parent.parent / "src"
    if not src_path.exists():
        print("❌ src/ directory not found")
        return False
    
    # Add to path for testing
    sys.path.insert(0, str(src_path))
    
    try:
        import config
        import generator
        import ai_service
        print("✅ Core modules accessible")
        return True
    except ImportError as e:
        print(f"❌ Core module import error: {e}")
        return False

def start_server():
    """Start the FastAPI server"""
    print("\n🚀 Starting PAPER-CODE Web GUI...")
    print("📍 Server will be available at: http://localhost:8000")
    print("🔄 Press Ctrl+C to stop the server")
    print("\n" + "="*50)
    
    try:
        # Import and run the main app
        import uvicorn
        
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
        
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"\n❌ Server error: {e}")
        print("💡 Try running: python main.py directly")

def main():
    """Main entry point"""
    print("🌐 PAPER-CODE Web GUI Launcher")
    print("="*30)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check core modules
    if not check_src_module():
        sys.exit(1)
    
    # Start server
    start_server()

if __name__ == "__main__":
    main()
