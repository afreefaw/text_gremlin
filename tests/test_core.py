import unittest
from pathlib import Path
import json
import tempfile
import shutil
from unittest.mock import patch, MagicMock

from document_extractor import extract_text
from document_extractor.processor import DocumentProcessor

class TestDocumentProcessor(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_files = {
            'test1.pdf': b'PDF content',
            'test2.pptx': b'PPTX content',
            'test3.docx': b'DOCX content',
            'subdir/test4.pdf': b'Nested PDF content'
        }
        
        # Create test files
        for path, content in self.test_files.items():
            file_path = Path(self.temp_dir) / path
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_bytes(content)
        
        self.processor = DocumentProcessor()
    
    def tearDown(self):
        shutil.rmtree(self.temp_dir)
    
    def test_file_traversal(self):
        """Test recursive file traversal"""
        files = list(self.processor._find_documents(Path(self.temp_dir)))
        self.assertEqual(len(files), 4)
        
        # Test non-recursive
        files = list(self.processor._find_documents(Path(self.temp_dir), recursive=False))
        self.assertEqual(len(files), 3)  # Excludes nested file
    
    def test_file_type_filtering(self):
        """Test file type filtering"""
        # Only PDF files
        files = list(self.processor._find_documents(
            Path(self.temp_dir),
            recursive=True,  # Need recursive to find PDF in subdirectory
            file_types=['pdf']
        ))
        self.assertEqual(len(files), 2)
        self.assertTrue(all(f.suffix == '.pdf' for f in files))
        
        # Multiple types
        files = list(self.processor._find_documents(
            Path(self.temp_dir),
            file_types=['pdf', 'pptx']
        ))
        self.assertEqual(len(files), 3)
    
    @patch('document_extractor.extractors.pdf.PDFExtractor.extract')
    def test_document_processing(self, mock_extract):
        """Test document processing with mocked extractor"""
        mock_extract.return_value = "Extracted text"
        
        result = next(self.processor.process_documents(
            str(Path(self.temp_dir) / 'test1.pdf')
        ))
        
        self.assertEqual(result['content'], "Extracted text")
        self.assertIsNone(result['error'])
        self.assertEqual(result['file_type'], 'pdf')

class TestExtractText(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = Path(self.temp_dir) / 'test.pdf'
        self.test_file.write_bytes(b'PDF content')
    
    def tearDown(self):
        shutil.rmtree(self.temp_dir)
    
    @patch('document_extractor.extractors.pdf.PDFExtractor.extract')
    def test_extract_text(self, mock_extract):
        """Test extract_text function"""
        mock_extract.return_value = "Extracted text"
        
        results = list(extract_text(
            str(self.temp_dir),
            file_types=['pdf']
        ))
        
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['content'], "Extracted text")
    
    @patch('document_extractor.extractors.pdf.PDFExtractor.extract')
    def test_extract_text_with_output(self, mock_extract):
        """Test extract_text function with file output"""
        mock_extract.return_value = "Extracted text"
        output_path = Path(self.temp_dir) / 'output.json'
        
        results = list(extract_text(
            str(self.test_file),
            output_path=str(output_path),
            file_types=['pdf']
        ))
        
        self.assertEqual(len(results), 1)
        
        with open(output_path) as f:
            data = json.load(f)
        
        self.assertEqual(len(data['documents']), 1)
        self.assertEqual(data['documents'][0]['content'], "Extracted text")

if __name__ == '__main__':
    unittest.main()