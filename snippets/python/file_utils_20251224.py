"""
File Utility Functions
"""
import os
import json
from pathlib import Path

def read_json(filepath):
    """Read JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

def write_json(filepath, data, indent=2):
    """Write data to JSON file."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=indent)

def list_files(directory, extension=None):
    """List files in directory."""
    path = Path(directory)
    if extension:
        return list(path.glob(f"*.{extension}"))
    return list(path.iterdir())

def get_file_size(filepath):
    """Get file size in human readable format."""
    size = os.path.getsize(filepath)
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"

# Example
if __name__ == "__main__":
    print(f"Current dir files: {len(list_files('.'))}")
