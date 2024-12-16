"""
LibGenX common module.
"""

from sys import argv
from json import load

def get_cli_args():
    """Parse arguments from the command line."""
    query = argv[1] if len(argv) > 1 else None
    seq = argv[2] if len(argv) > 2 else None
    return query, seq

def load_config():
    """Load configuration from config.json."""
    with open("config.json", "r") as f:
        return load(f)
