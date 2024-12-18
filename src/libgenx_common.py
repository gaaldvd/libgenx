"""
LibGenX common module.
"""

from sys import argv
from json import load
from re import findall
from libgentools import FILTERS, FilterError

def load_config():
    """Load configuration from config.json."""
    with open("config.json", "r") as f:
        return load(f)

def get_cli_args():
    """Parse arguments from the command line."""
    query = argv[1] if len(argv) > 1 else None
    seq = argv[2] if len(argv) > 2 else None
    return query, seq

def parse_filter_seq(seq):
    """Interpret sequence and return filtering parameters."""

    # filtering mode
    if "-x" in seq:
        mode = "exact"
        seq = seq.replace("-x", "").strip().replace("  ", " ")
    else:
        mode = "partial"

    # translate to the corresponding key-value pairs from libgentools.FILTERS
    matches = findall(r"-(\w) (.*?)(?= -\w|$)", seq)
    filters_raw = {f"-{key}": value.strip() for key, value in matches}

    # validate filters
    filters = {}
    for key, value in filters_raw.items():
        if key in FILTERS:
            filters[FILTERS[key]] = value
        else:
            raise FilterError(f"Invalid filter: {key}")

    return filters, mode