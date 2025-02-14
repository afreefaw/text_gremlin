"""
Document extractors package.
"""

from .pdf import PDFExtractor
from .pptx import PPTXExtractor

__all__ = ["PDFExtractor", "PPTXExtractor"]