# package-name

<!-- Badges: replace OWNER/REPO after creating from template -->
[![CI](https://github.com/Yasir323/python-project-template/actions/workflows/ci.yml/badge.svg)](https://github.com/Yasir323/REPO/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/package-name)](https://pypi.org/project/package-name/)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](pyproject.toml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

One-paragraph pitch: what problem this solves and for whom.

## Install

```bash
pip install package-name
```

## Quickstart

```python
# Smallest possible working example.
```

## Why this exists

Link to the design writeup / war story. See [docs/adr/](docs/adr/) for
decision records.

## Development

```bash
make install   # venv + dev tools + pre-commit hooks
make all       # lint + typecheck + tests with coverage gate
```

| Target      | What it does                              |
| ----------- | ----------------------------------------- |
| `lint`      | ruff check + format check                 |
| `fmt`       | auto-fix and reformat                     |
| `typecheck` | mypy --strict                             |
| `test`      | unit tests                                |
| `itest`     | integration tests (real infrastructure)   |
| `cov`       | unit tests with 90% coverage gate         |

---

## Using this template (delete this section)

1. Create repo from template on GitHub.
2. Rename: `package-name` (3 places in `pyproject.toml`, badges above)
   and the `src/package_name/` directory.
3. `make install && make all` — must pass before the first real commit.
4. Delete `src/package_name/example.py`, its tests, and this section.
