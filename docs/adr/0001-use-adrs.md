# ADR-0001: Record Architecture Decisions as ADRs

- **Status:** accepted
- **Date:** 2026-06-13

## Context and Problem Statement

Design decisions (database choice, consistency model, delivery
semantics) are made throughout a project's life. Without a record, the
reasoning evaporates — future contributors (including the author) can
only see *what* was decided, not *why*, and re-litigate settled
questions.

## Decision Drivers

- Decisions must be reviewable in PRs alongside the code they affect.
- Zero tooling cost; plain markdown in the repo.
- Interview/portfolio value: visible architectural reasoning.

## Considered Options

1. MADR-style ADRs in `docs/adr/`
2. Design docs in a wiki / Notion
3. No formal record (decisions live in PR descriptions)

## Decision Outcome

Chosen option: **MADR-style ADRs in `docs/adr/`** — versioned with the
code, reviewed like code, and discoverable by anyone reading the repo.

### Consequences

- Good: reasoning survives; superseded decisions stay visible.
- Bad: small writing overhead per significant decision.
- Follow-up: every significant design decision gets an ADR using
  [0000-template.md](0000-template.md); trivial choices do not.
