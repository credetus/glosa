"""glosa."""

from importlib.metadata import version

from glosa.core import Glosa
from glosa.storage import BaseStorageManager

__all__ = ["BaseStorageManager", "Glosa", "__version__"]
__version__ = version("glosa")
