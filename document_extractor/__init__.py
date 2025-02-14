"""
Simple document text extraction library.
"""

__version__ = "0.1.0"

from .extractors.pdf import PDFExtractor
from .extractors.pptx import PPTXExtractor

__all__ = ["PDFExtractor", "PPTXExtractor"]