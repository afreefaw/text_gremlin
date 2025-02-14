from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any

@dataclass
class DocumentResult:
    """Class representing the result of document text extraction."""
    file_path: str
    file_name: str
    file_type: str
    date_created: datetime
    date_modified: datetime
    extraction_time: datetime
    content: str
    error: Optional[str] = None

    @classmethod
    def from_path(cls, path: Path, content: str = "", error: Optional[str] = None) -> 'DocumentResult':
        """Create a DocumentResult instance from a file path."""
        stats = path.stat()
        return cls(
            file_path=str(path.absolute()),
            file_name=path.name,
            file_type=path.suffix.lstrip('.').lower(),
            date_created=datetime.fromtimestamp(stats.st_ctime),
            date_modified=datetime.fromtimestamp(stats.st_mtime),
            extraction_time=datetime.now(),
            content=content,
            error=error
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert the document result to a dictionary."""
        data = asdict(self)
        # Convert datetime objects to ISO format strings
        for key in ['date_created', 'date_modified', 'extraction_time']:
            data[key] = data[key].isoformat()
        return data