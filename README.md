# Document Text Extractor

A Python library for extracting text from PDF, PowerPoint (PPTX), and Word (DOCX) files, with both API and GUI interfaces.

## Features

- Extract text from multiple document types:
  - PDF files using PyMuPDF
  - PowerPoint (PPTX) files using python-pptx
  - Word (DOCX) files
- Recursive directory traversal
- Multiple output modes (streaming or file-based)
- User-friendly GUI interface
- Simple, clean API
- No dependencies on large frameworks
- Type hints included

## Installation

1. Clone this repository
2. Install requirements:
```bash
pip install -r requirements.txt
```

## GUI Usage

The application includes a graphical interface for easy text extraction:

1. Run the GUI:
```bash
python gui.py
```

2. Features:
- Select input directory containing documents
- Choose output JSON file location
- Filter by file types (PDF, PPTX, DOCX)
- Toggle recursive directory scanning
- Real-time progress tracking
- Cancellable operations

## API Usage

### Output Format

Each extraction result is a JSON object with the following structure:

```json
{
  "file_path": "path/to/document.pdf",      // Full path to the processed file
  "file_name": "document.pdf",              // Name of the file
  "file_type": "pdf",                       // Type of document (pdf, docx, pptx)
  "date_created": "2025-02-13T23:05:08.350199",    // File creation timestamp
  "date_modified": "2025-02-07T00:54:09.536225",   // File modification timestamp
  "extraction_time": "2025-02-14T00:50:49.808537", // When the text was extracted
  "content": {
    // Same metadata fields as above
    "file_path": "path/to/document.pdf",
    "file_name": "document.pdf",
    "file_type": "pdf",
    "date_created": "2025-02-13T23:05:08.350199",
    "date_modified": "2025-02-07T00:54:09.536225",
    "extraction_time": "2025-02-14T00:50:49.808537",
    "content": "Extracted text content from the document...",
    "error": null  // Error message if extraction failed, null otherwise
  },
  "error": null    // Error message if extraction failed, null otherwise
}
```

### Basic Text Extraction

```python
from document_extractor import extract_text

# Extract text from a single file (streams results)
for result in extract_text("path/to/document.pdf"):
    if not result['error']:
        print(f"File: {result['file_name']}")
        print(f"Created: {result['date_created']}")
        print(f"Content: {result['content']['content']}")

# Extract text from a directory (recursive by default)
for result in extract_text("path/to/documents/"):
    if not result['error']:
        print(f"File: {result['file_name']}")
        print(f"Type: {result['file_type']}")
        print(f"Modified: {result['date_modified']}")
        print(f"Content: {result['content']['content']}")
```

### Output Modes

The library supports two output modes:

1. Stream mode (default) - yields results as they are processed:
```python
# Stream results
for result in extract_text("path/to/documents/", output_mode="stream"):
    if not result['error'] and not result['content']['error']:
        print(f"Content: {result['content']['content']}")
```

2. File mode - writes all results to a JSON file:
```python
# Write to file
extract_text(
    "path/to/documents/",
    output_mode="file",
    output_name="output.json"
)
```

### Additional Options

```python
# Process specific file types only
results = extract_text(
    "path/to/documents/",
    file_types=['pdf', 'pptx']  # Only process PDF and PPTX files
)

# Disable recursive directory traversal
results = extract_text(
    "path/to/documents/",
    recursive=False  # Only process files in top-level directory
)
```

See `example.py` for more detailed usage examples.

## Requirements

- PyMuPDF>=1.23.8
- python-pptx>=0.6.21
- tkinter (included with Python)

## Error Handling

The library provides detailed error information in the extraction results:

```python
for result in extract_text("path/to/documents/"):
    if result['error']:
        print(f"Error processing {result['file_name']}: {result['error']}")
    else:
        print(f"Successfully extracted text from {result['file_name']}")
```

Common errors:
- `FileNotFoundError` if input path doesn't exist
- `ValueError` if output_mode is "file" but no output_name provided
- Individual file processing errors are captured in the result's 'error' field

## License

MIT License file types (PDF, PPTX, DOCX)
- Toggle recursive directory scanning
- Real-time progress tracking
- Cancellable operations

![Text Gremlin GUI](docs/gui.png)

## API Usage

### Basic Text Extraction

```python
from document_extractor import extract_text

# Extract text from a single file (streams results)
for result in extract_text("path/to/document.pdf"):
    print(result['content'])

# Extract text from a directory (recursive by default)
for result in extract_text("path/to/documents/"):
    print(f"File: {result['file_name']}")
    print(f"Content: {result['content']}")
```

### Output Modes

The library supports two output modes:

1. Stream mode (default) - yields results as they are processed:
```python
# Stream results
for result in extract_text("path/to/documents/", output_mode="stream"):
    print(result['content'])
```

2. File mode - writes all results to a JSON file:
```python
# Write to file
extract_text(
    "path/to/documents/",
    output_mode="file",
    output_name="output.json"
)
```

### Additional Options

```python
# Process specific file types only
results = extract_text(
    "path/to/documents/",
    file_types=['pdf', 'pptx']  # Only process PDF and PPTX files
)

# Disable recursive directory traversal
results = extract_text(
    "path/to/documents/",
    recursive=False  # Only process files in top-level directory
)
```

See `example.py` for more detailed usage examples.

## Requirements

- PyMuPDF>=1.23.8
- python-pptx>=0.6.21
- tkinter (included with Python)

## Error Handling

The library provides detailed error information in the extraction results:

```python
for result in extract_text("path/to/documents/"):
    if result['error']:
        print(f"Error processing {result['file_name']}: {result['error']}")
    else:
        print(f"Successfully extracted text from {result['file_name']}")
```

Common errors:
- `FileNotFoundError` if input path doesn't exist
- `ValueError` if output_mode is "file" but no output_name provided
- Individual file processing errors are captured in the result's 'error' field

## License

MIT License