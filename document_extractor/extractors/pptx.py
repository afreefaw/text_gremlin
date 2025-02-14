"""
PowerPoint text extraction using python-pptx.
"""

from pathlib import Path
from typing import Union
from pptx import Presentation


class PPTXExtractor:
    """Extracts text from PowerPoint files using python-pptx."""
    
    @staticmethod
    def extract_text(file_path: Union[str, Path]) -> str:
        """
        Extract text from a PowerPoint file.
        
        Args:
            file_path: Path to the PowerPoint file (string or Path object)
            
        Returns:
            str: Extracted text from the presentation
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            ValueError: If the file is not a PPTX
        """
        file_path = Path(file_path)
        
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
            
        if file_path.suffix.lower() != '.pptx':
            raise ValueError(f"Not a PPTX file: {file_path}")
        
        text = []
        prs = Presentation(str(file_path))
        
        # Extract text from each slide's shapes
        for slide in prs.slides:
            for shape in slide.shapes:
                if hasattr(shape, "text") and shape.text.strip():
                    text.append(shape.text.strip())
        
        return "\n".join(text)