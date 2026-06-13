# Contributing

## Setup

```bash
make install
```

Requires [uv](https://docs.astral.sh/uv/). Python 3.11+ is fetched
automatically.

## Workflow

1. Branch from `main`.
2. `make all` must pass locally (CI runs the same gates).
3. Commit messages follow
   [Conventional Commits](https://www.conventionalcommits.org/)
   (`feat:`, `fix:`, `docs:` …) — enforced by a commit-msg hook.
4. Significant design decisions get an ADR in `docs/adr/`.
5. Open a PR; the template will guide you.

## Quality bar

- mypy `--strict` clean
- 90%+ coverage on changed code
- Integration tests use real infrastructure (testcontainers), not mocks
