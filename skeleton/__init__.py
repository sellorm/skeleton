"""
A Simple skeleton python package
"""

try:
    from importlib import metadata
except ImportError:
    # Running on pre-3.8 Python; use importlib-metadata package
    import importlib_metadata as metadata

__version__ = metadata.version("skeleton")


def info():
    """
    Prints a brief message

    """
    print("This is a skeleton package")
