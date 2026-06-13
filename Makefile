# Every target runs through uv so the venv is always consistent.
.PHONY: install lint fmt typecheck test itest cov all

install:        ## create venv, install package + dev tools, install hooks
	uv sync
	uv run pre-commit install --install-hooks

lint:           ## ruff lint + format check (no changes made)
	uv run ruff check .
	uv run ruff format --check .

fmt:            ## auto-fix lint issues and reformat
	uv run ruff check --fix .
	uv run ruff format .

typecheck:      ## mypy --strict over src and tests
	uv run mypy

test:           ## unit tests, fast, no infrastructure
	uv run pytest

itest:          ## integration tests (testcontainers etc.)
	uv run pytest tests/integration -m integration

cov:            ## unit tests with coverage gate (fail under 90%)
	uv run pytest --cov --cov-report=term --cov-report=xml

all: lint typecheck cov   ## everything CI runs
