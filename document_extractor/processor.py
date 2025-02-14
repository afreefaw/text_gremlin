from datetime import datetime
import os
from pathlib import Path
from typing import Iterator, List, Optional, Dict, Any, Set
import json
from json import JSONEncoder
from datetime import datetime

class DateTimeEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

from .models import DocumentResult
from .extractors.pdf import PDFExtractor
from .extractors.pptx import PPTXExtractor
from .extractors.docx import DOCXExtractor


class DocumentProcessor:
    """Core processing engine for document text extraction."""
    
    def __init__(self):
        """Initialize the document processor."""
        self.extractors = {
            "pdf": PDFExtractor(),
            "pptx": PPTXExtractor(),
            "docx": DOCXExtractor()
        }
    
    def _find_documents(
        self,
        input_path: Path,
        recursive: bool = True,
        file_types: Optional[List[str]] = None
    ) -> Iterator[Path]:
        """Find document paths from the input path.
        
        Args:
            input_path: Path to file or directory
            recursive: Whether to recursively search directories
            file_types: List of file types to process (without dots)
            
        Yields:
            Path objects for each document found
        """
        supported_types = set(file_types) if file_types else {"pdf", "pptx", "docx"}
        
        if input_path.is_file():
            if input_path.suffix.lstrip('.').lower() in supported_types:
                yield input_path
            return

        for entry in os.scandir(str(input_path)):
            entry_path = Path(entry.path)
            if entry.is_file():
                if entry_path.suffix.lstrip('.').lower() in supported_types:
                    yield entry_path
            elif entry.is_dir() and recursive:
                yield from self._find_documents(entry_path, recursive, file_types)
    
    def _process_single_document(self, path: Path) -> DocumentResult:
        """Process a single document.
        
        Args:
            path: Path to the document
            
        Returns:
            DocumentResult containing extraction results
        """
        file_type = path.suffix.lstrip('.').lower()
        extractor = self.extractors.get(file_type)
        
        try:
            if not extractor:
                raise ValueError(f"No extractor available for file type: {file_type}")
            
            result = extractor.extract(path)
            if result.error:
                return result
            return DocumentResult.from_path(path, result.content)
        except Exception as e:
            return DocumentResult.from_path(path, "", str(e))
    
    def process_documents(
        self,
        input_path: str,
        output_path: Optional[str] = None,
        recursive: bool = False,
        file_types: Optional[List[str]] = None
    ) -> Iterator[Dict[str, Any]]:
        """Process documents and handle output.
        
        Args:
            input_path: Path to file or directory to process
            output_path: Optional path to write JSON output
            recursive: Whether to recursively search directories
            file_types: List of file types to process
            
        Yields:
            Dictionary containing extraction results for each document
        """
        path = Path(input_path)
        documents = []
        
        for doc_path in self._find_documents(path, recursive, file_types):
            result = self._process_single_document(doc_path)
            doc_dict = result.to_dict()
            documents.append(doc_dict)
            yield doc_dict
        
        if output_path:
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump({"documents": documents}, f, indent=2, cls=DateTimeEncoder)