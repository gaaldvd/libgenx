"""
LibGenX common module.
"""

from sys import argv
from json import load

def get_query_arg():
    """Parse query from the command line."""
    return argv[1] if len(argv) > 1 else None

def load_config():
    """Load configuration from config.json."""
    with open("config.json", "r") as f:
        return load(f)
