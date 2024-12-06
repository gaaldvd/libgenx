"""
LibGenX common module.
"""

import sys


def get_query_arg():
    """Parse query from the command line."""
    return sys.argv[1] if len(sys.argv) > 1 else None
