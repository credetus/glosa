from abc import ABC

import glosa
from glosa import BaseStorageManager, Glosa


class DummyStorageManager(BaseStorageManager):
    pass


class DummyGlosa(Glosa):
    pass


def test_classes_are_abstract_bases() -> None:
    assert issubclass(Glosa, ABC)
    assert issubclass(BaseStorageManager, ABC)


def test_glosa_stores_storage_manager() -> None:
    storage_manager = DummyStorageManager()
    instance = DummyGlosa(storage_manager=storage_manager)
    assert instance.storage_manager is storage_manager


def test_version() -> None:
    assert isinstance(glosa.__version__, str)
