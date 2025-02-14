# Text Gremlin Implementation Plan

## Stage 1: Core Module Development

### Objectives
- Implement standardized JSON output format
- Add batch processing and file writing capabilities
- Develop streaming functionality for concurrent processing
- Create flexible output modes
- Maintain existing text extraction functionality

### Tasks

1. **Create Base Data Structures**
   - Define JSON output schema
   ```python
   {
     "metadata": {
       "timestamp": "2024-02-13T22:51:15",
       "version": "1.0.0",
       "file_types_processed": ["pdf", "pptx"]
     },
     "documents": [
       {
         "file_path": "path/to/doc.pdf",
         "file_name": "doc.pdf",
         "file_type": "pdf",
         "date_created": "2024-02-13T20:30:00",
         "date_modified": "2024-02-13T22:45:00",
         "extraction_time": "2024-02-13T22:51:15",
         "content": "extracted text here",
         "error": null  # or error message if failed
       }
     ]
   }
   ```
   - Implement document result class for standardized processing

2. **Develop Core Processing Engine**
   - Create DocumentProcessor class with streaming support
   ```python
   class DocumentProcessor:
       def process_documents(self, input_path, **kwargs):
           for doc in self._stream_documents(input_path):
               yield self._process_single_document(doc)
   ```
   - Implement recursive directory traversal
   - Add file type filtering
   - Create batch processing logic

3. **Implement Output Handlers**
   - Create OutputHandler base class
   - Implement FileOutputHandler for JSON file writing
   - Add StreamingOutputHandler for text responses
   - Develop batch writing mechanism for file output

4. **Update Existing Extractors**
   - Modify PDF extractor to work with new structure
   - Update PPTX extractor for compatibility
   - Add error handling and reporting

5. **Create Main Interface**
   ```python
   def extract_text(
       input_path: Union[str, Path],
       output_name: Optional[str] = None,
       output_mode: str = "stream",
       file_types: Optional[List[str]] = None,
       recursive: bool = False
   ) -> Union[Iterator[Dict], None]:
       # Implementation
   ```

### Testing Considerations
- Unit tests for each component:
  - Document processing logic
  - File traversal and filtering
  - Output handling
  - Batch processing
- Integration tests:
  - End-to-end processing
  - Different output modes
  - Error handling
- Performance tests:
  - Large document processing
  - Memory usage monitoring
  - Batch writing efficiency

## Stage 2: GUI Development

### Objectives
- Create user-friendly interface
- Integrate core functionality
- Provide visual feedback
- Implement progress tracking

### Tasks

1. **Design Basic GUI Layout**
   - Create main window with tkinter
   ```python
   class TextGremlinGUI:
       def __init__(self):
           self.root = tk.Tk()
           self.root.title("Text Gremlin")
           # Setup UI components
   ```
   - Add input/output path selection
   - Implement options panel
   - Create progress display area

2. **Add Interactive Components**
   - Folder browser button
   - File type checkboxes
   - Output mode selection
   - Recursive search toggle
   - Extract button

3. **Implement Progress Tracking**
   - Add progress bar
   - Create status messages
   - Display current file being processed
   - Show completion statistics

4. **Integrate Core Functionality**
   - Connect GUI actions to core module
   - Handle background processing
   - Implement cancellation
   - Add error display

5. **Add Resume Capability**
   - Save progress state
   - Implement checkpoint system
   - Add resume option in GUI
   - Create progress recovery logic

### Testing Considerations
- GUI component tests:
  - Button functionality
  - Input validation
  - Display updates
- Integration tests:
  - Core module integration
  - Progress tracking accuracy
  - Resume functionality
- User experience tests:
  - Error message clarity
  - Progress feedback
  - Intuitive controls

## Implementation Notes

### Stage 1 Priority Tasks
1. JSON output structure and batch processing
2. Streaming implementation
3. Output mode handling
4. Core function interface
5. Basic test suite

### Stage 2 Priority Tasks
1. Basic GUI framework
2. Core functionality integration
3. Progress tracking
4. Resume capability
5. GUI tests

### Dependencies
- Existing: fitz (PyMuPDF), python-pptx
- New: tkinter (GUI)

### Considerations
- Memory management for large directories
- Error handling and recovery
- Progress persistence
- User feedback mechanisms