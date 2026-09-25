# glosa

Glosa.

## Installation

```bash
uv add glosa
# or
pip install glosa
```

## Usage

```python
from glosa import BaseStorageManager, Glosa


class MyStorageManager(BaseStorageManager):
    pass


class MyGlosa(Glosa):
    pass


app = MyGlosa(storage_manager=MyStorageManager())
```

## Development

```bash
uv sync                      # create .venv and install dev dependencies
uv run pytest --cov          # run tests with coverage
uv run ruff check .          # lint
uv run ruff format .         # format
uv run ty check              # type check
uv build                     # build sdist + wheel into dist/
```

## Releasing

Releases are published to PyPI by GitHub Actions using
[trusted publishing](https://docs.pypi.org/trusted-publishers/) (no API tokens).

1. Bump the version: `uv version --bump patch` (or `minor` / `major`).
2. Commit and push to `main`.
3. Tag and push: `git tag v$(uv version --short) && git push --tags`.

The `Release` workflow runs CI, verifies the tag matches `pyproject.toml`,
builds and smoke-tests the distributions, publishes to PyPI, and creates a
GitHub Release with auto-generated notes.

## License

MIT
