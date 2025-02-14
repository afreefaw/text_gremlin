"""
PDF text extraction using PyMuPDF (fitz).
"""

import fitz
from pathlib import Path
from typing import Union

from ..models import DocumentResult

class PDFExtractor:
    """Extracts text from PDF files using PyMuPDF (fitz)."""
    
    @staticmethod
    def extract(file_path: Union[str, Path]) -> DocumentResult:
        """
        Extract text from a PDF file.
        
        Args:
            file_path: Path to the PDF file (string or Path object)
            
        Returns:
            DocumentResult: Extraction result containing the text and metadata
        """
        file_path = Path(file_path)
        
        try:
            if not file_path.exists():
                raise FileNotFoundError(f"File not found: {file_path}")
                
            if file_path.suffix.lower() != '.pdf':
                raise ValueError(f"Not a PDF file: {file_path}")
            
            text = ""
            with fitz.open(str(file_path)) as doc:
                # Extract text from each page
                for page in doc:
                    text += page.get_text()
                    
            return DocumentResult.from_path(file_path, content=text.strip())
            
        except (FileNotFoundError, ValueError) as e:
            # Pass through common errors with their messages
            return DocumentResult.from_path(file_path, error=str(e))
        except fitz.fitz.FileDataError as e:
            return DocumentResult.from_path(file_path, error=f"Invalid or corrupted PDF file: {e}")
        except Exception as e:
            return DocumentResult.from_path(file_path, error=f"Unexpected error during PDF extraction: {e}")

    @staticmethod
    def extract_text(file_path: Union[str, Path]) -> str:
        """
        Legacy method for backward compatibility.
        
        Args:
            file_path: Path to the PDF file (string or Path object)
            
        Returns:
            str: Extracted text from the PDF
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            ValueError: If the file is not a PDF
        """
        result = PDFExtractor.extract(file_path)
        if result.error:
            raise ValueError(result.error)
        return result.content