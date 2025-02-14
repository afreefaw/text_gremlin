from .processor import DocumentProcessor

def extract_text(
    input_path: str,
    output_path: str = None,
    recursive: bool = False,
    file_types: list[str] = None
):
    """Extract text from documents.
    
    Args:
        input_path: Path to file or directory to process
        output_path: Optional path to write JSON output
        recursive: Whether to recursively search directories
        file_types: List of file types to process
        
    Returns:
        Iterator of document results
    """
    processor = DocumentProcessor()
    return processor.process_documents(
        input_path,
        output_path=output_path,
        recursive=recursive,
        file_types=file_types
    )