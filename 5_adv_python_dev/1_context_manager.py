"""
suppress_stdout, which temporarily redirects the standard output (stdout) to an in-memory buffer. This effectively prevents any output generated within the with statement's code block from being displayed on the console.
"""

import sys
import io
from contextlib import contextmanager


@contextmanager
def suppress_stdout():
    """Temporarily suppresses stdout."""
    original_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        yield
    finally:
        sys.stdout = original_stdout


# Example usage:
with suppress_stdout():
    print("This won't be displayed.")

print("This will be displayed.")
