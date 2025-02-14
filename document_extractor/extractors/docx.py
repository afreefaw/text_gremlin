from pathlib import Path
from docx import Document

class DOCXExtractor:
    """Extractor for DOCX files using python-docx."""
    
    def extract(self, path: Path) -> str:
        """Extract text content from a DOCX file.
        
        Args:
            path: Path to the DOCX file
            
        Returns:
            Extracted text content as a string
            
        Raises:
            Exception: If there's an error reading the file
        """
        doc = Document(str(path))
        
        # Extract text from paragraphs
        paragraphs = [paragraph.text for paragraph in doc.paragraphs if paragraph.text.strip()]
        
        # Extract text from tables
        table_text = []
        for table in doc.tables:
            for row in table.rows:
                cells = [cell.text.strip() for cell in row.cells if cell.text.strip()]
                if cells:
                    table_text.append(" | ".join(cells))
        
        # Combine all text with appropriate spacing
        all_text = paragraphs + table_text
        return "\n\n".join(all_text)