# src/ai_service.py

"""
AI Service Module for PAPER-CODE.
Handles integration with OpenAI API for generating project descriptions.
"""

import os
import json
from typing import Optional, Dict, Any
from dotenv import load_dotenv
import openai
from openai import OpenAI

# Load environment variables from .env file if it exists
load_dotenv()

class AIService:
    """
    Service class for AI-powered features in PAPER-CODE.
    Currently supports OpenAI API for generating project descriptions.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the AI service.
        
        Args:
            api_key (Optional[str]): OpenAI API key. If not provided, will try to get from environment.
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.client = None
        
        if self.api_key:
            try:
                self.client = OpenAI(api_key=self.api_key)
            except Exception as e:
                print(f"⚠️ Failed to initialize OpenAI client: {e}")
                self.client = None
    
    def is_available(self) -> bool:
        """Check if AI service is available and configured."""
        return self.client is not None
    
    def generate_project_description(self, project_name: str, project_type: str, tech_stack: str, libraries: list = None, user_hint: str = "") -> str:
        """
        Generate a comprehensive project description using AI.
        
        Args:
            project_name (str): Name of the project
            project_type (str): Type of project (Frontend, Backend, etc.)
            tech_stack (str): Technology stack being used
            libraries (list): List of selected libraries
            user_hint (str): Optional user hint about the project
            
        Returns:
            str: Generated project description
        """
        if not self.is_available():
            return self._generate_fallback_description(project_name, project_type, tech_stack, libraries)
        
        try:
            # Build the prompt
            libraries_str = ", ".join(libraries) if libraries else "None"
            
            system_prompt = """You are an expert technical writer and software architect. 
Generate a concise but comprehensive project description (2-3 paragraphs) that helps AI coding assistants understand the project's purpose, architecture, and goals.

Focus on:
1. What the project does and its main purpose
2. Key technical decisions and architecture patterns
3. Target users and use cases
4. Development goals and constraints

Keep it professional, clear, and specific. Avoid generic statements."""

            user_prompt = f"""Project Details:
- Name: {project_name}
- Type: {project_type}
- Tech Stack: {tech_stack}
- Libraries: {libraries_str}
{f'- User Hint: {user_hint}' if user_hint else ''}

Generate a project description that will help AI coding assistants understand this project better."""

            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            print(f"⚠️ AI generation failed: {e}")
            return self._generate_fallback_description(project_name, project_type, tech_stack, libraries)
    
    def _generate_fallback_description(self, project_name: str, project_type: str, tech_stack: str, libraries: list = None) -> str:
        """
        Generate a fallback description when AI is not available.
        
        Args:
            project_name (str): Name of the project
            project_type (str): Type of project
            tech_stack (str): Technology stack
            libraries (list): List of libraries
            
        Returns:
            str: Fallback project description
        """
        libraries_str = f" with {', '.join(libraries)}" if libraries else ""
        
        return f"""{project_name} is a modern {project_type.lower()} application built with {tech_stack}{libraries_str}. 

This project follows best practices and industry standards for maintainable, scalable development. The architecture is designed to provide a solid foundation for future enhancements while ensuring code quality and developer productivity.

The project leverages modern development tools and workflows to streamline the development process and maintain high code quality standards throughout the lifecycle."""
