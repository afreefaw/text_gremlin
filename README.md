# Document Text Extractor

A simple Python library for extracting text from PDF and PowerPoint (PPTX) files.

## Features

- Extract text from PDF files using PyMuPDF
- Extract text from PowerPoint (PPTX) files using python-pptx
- Simple, clean API
- No dependencies on large frameworks
- Type hints included

## Installation

1. Clone this repository
2. Install requirements:
```bash
pip install -r requirements.txt
```

## Usage

### PDF Text Extraction

```python
from document_extractor import PDFExtractor

# Extract text from a PDF file
text = PDFExtractor.extract_text("path/to/document.pdf")
print(text)
```

### PowerPoint Text Extraction

```python
from document_extractor import PPTXExtractor

# Extract text from a PowerPoint file
text = PPTXExtractor.extract_text("path/to/presentation.pptx")
print(text)
```

See `example.py` for more detailed usage examples.

## Requirements

- PyMuPDF>=1.23.8
- python-pptx>=0.6.21

## Error Handling

Both extractors will raise:
- `FileNotFoundError` if the file doesn't exist
- `ValueError` if the file extension doesn't match the expected type

## License

MIT License