"""
CodeAlpha Task Automation Package
----------------------------------
Contains core modules for file organization, data extraction, and speed optimization.
"""

from .file_organizer import organize_files
from .data_extractor import extract_emails

__version__ = "1.0.0"
__all__ = ["organize_files", "extract_emails"]