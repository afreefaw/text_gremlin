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