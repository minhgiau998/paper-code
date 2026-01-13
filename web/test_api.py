"""
Test script for PAPER-CODE Web GUI API endpoints
"""

import sys
import os
from pathlib import Path

# Add src directory to path
sys.path.append(str(Path(__file__).parent.parent / "src"))

def test_imports():
    """Test if all required modules can be imported"""
    try:
        from config import PROJECT_TYPES, TECH_STACKS, LIBRARIES
        from generator import DocGenerator
        from ai_service import AIService
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_config_structure():
    """Test if configuration data is properly structured"""
    try:
        from config import PROJECT_TYPES, TECH_STACKS, LIBRARIES
        
        # Check if PROJECT_TYPES is a non-empty list
        if not isinstance(PROJECT_TYPES, list) or len(PROJECT_TYPES) == 0:
            print("❌ PROJECT_TYPES is empty or not a list")
            return False
        
        # Check if TECH_STACKS is a dict with valid project types
        if not isinstance(TECH_STACKS, dict):
            print("❌ TECH_STACKS is not a dict")
            return False
        
        # Check if LIBRARIES is a dict
        if not isinstance(LIBRARIES, dict):
            print("❌ LIBRARIES is not a dict")
            return False
        
        print(f"✅ Configuration structure valid:")
        print(f"   - Project Types: {len(PROJECT_TYPES)}")
        print(f"   - Tech Stacks: {len(TECH_STACKS)}")
        print(f"   - Libraries: {len(LIBRARIES)}")
        return True
        
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False

def test_generator():
    """Test if DocGenerator can be instantiated"""
    try:
        from generator import DocGenerator
        
        # Create a temporary directory for testing
        import tempfile
        temp_dir = tempfile.mkdtemp()
        
        # Test generator instantiation
        generator = DocGenerator(temp_dir, None, False)
        print("✅ DocGenerator instantiation successful")
        
        # Clean up
        import shutil
        shutil.rmtree(temp_dir)
        return True
        
    except Exception as e:
        print(f"❌ DocGenerator test failed: {e}")
        return False

def test_ai_service():
    """Test if AIService can be instantiated"""
    try:
        from ai_service import AIService
        
        ai_service = AIService()
        available = ai_service.is_available()
        print(f"✅ AIService instantiation successful (Available: {available})")
        return True
        
    except Exception as e:
        print(f"❌ AIService test failed: {e}")
        return False

def test_sample_generation():
    """Test a sample project generation"""
    try:
        from generator import DocGenerator
        import tempfile
        import shutil
        
        # Create temporary directory
        temp_dir = tempfile.mkdtemp()
        
        # Sample configuration
        sample_config = {
            "project_name": "Test Project",
            "description": "A test project for validation",
            "project_type": "Frontend",
            "tech_stack": "React",
            "libraries": ["Axios", "TailwindCSS"]
        }
        
        # Generate project
        generator = DocGenerator(temp_dir, None, False)
        generator.generate_project(sample_config)
        
        # Check if files were generated
        generated_files = list(Path(temp_dir).rglob("*"))
        generated_files = [f for f in generated_files if f.is_file()]
        
        if len(generated_files) > 0:
            print(f"✅ Sample generation successful ({len(generated_files)} files)")
            print(f"   Generated files: {[f.name for f in generated_files[:5]]}")
        else:
            print("❌ No files generated")
            return False
        
        # Clean up
        shutil.rmtree(temp_dir)
        return True
        
    except Exception as e:
        print(f"❌ Sample generation failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing PAPER-CODE Web GUI Components")
    print("=" * 50)
    
    tests = [
        ("Import Test", test_imports),
        ("Configuration Test", test_config_structure),
        ("DocGenerator Test", test_generator),
        ("AIService Test", test_ai_service),
        ("Sample Generation Test", test_sample_generation)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 {test_name}:")
        if test_func():
            passed += 1
        else:
            print(f"   ❌ {test_name} failed")
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Web GUI should work correctly.")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
