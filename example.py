"""
Example usage of document text extractors.
"""

from document_extractor import PDFExtractor, PPTXExtractor


def extract_pdf_example(pdf_path):
    """Example of PDF text extraction."""
    try:
        text = PDFExtractor.extract_text(pdf_path)
        print("=== PDF Text ===")
        print(text)
    except Exception as e:
        print(f"Error extracting PDF text: {e}")


def extract_pptx_example(pptx_path):
    """Example of PowerPoint text extraction."""
    try:
        text = PPTXExtractor.extract_text(pptx_path)
        print("=== PowerPoint Text ===")
        print(text)
    except Exception as e:
        print(f"Error extracting PowerPoint text: {e}")


if __name__ == "__main__":
    # Example usage
    pdf_file = "path/to/your/document.pdf"
    pptx_file = "path/to/your/presentation.pptx"
    
    print("Document Text Extractor Example\n")
    
    extract_pdf_example(pdf_file)
    print("\n" + "="*50 + "\n")
    extract_pptx_example(pptx_file)