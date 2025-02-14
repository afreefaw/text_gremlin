"""
PDF text extraction using PyMuPDF (fitz).
"""

import fitz
from pathlib import Path
from typing import Union


class PDFExtractor:
    """Extracts text from PDF files using PyMuPDF (fitz)."""
    
    @staticmethod
    def extract_text(file_path: Union[str, Path]) -> str:
        """
        Extract text from a PDF file.
        
        Args:
            file_path: Path to the PDF file (string or Path object)
            
        Returns:
            str: Extracted text from the PDF
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            ValueError: If the file is not a PDF
        """
        file_path = Path(file_path)
        
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
            
        if file_path.suffix.lower() != '.pdf':
            raise ValueError(f"Not a PDF file: {file_path}")
        
        text = ""
        with fitz.open(str(file_path)) as doc:
            # Extract text from each page
            for page in doc:
                text += page.get_text()
                
        return text.strip()