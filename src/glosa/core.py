"""Glosa base class."""

from abc import ABC

from glosa.storage import BaseStorageManager


class Glosa(ABC):  # noqa: B024 - abstract methods to be added
    """Abstract base class for Glosa."""

    def __init__(self, storage_manager: BaseStorageManager) -> None:
        self.storage_manager = storage_manager
