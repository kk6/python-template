# Claude Development Guide

This document serves as a reference for Claude when working with this project.

## Project Overview

This is a Python project template designed for use with Claude Code and VSCode.
It provides a modern development environment with automated tooling and best
practices.

## Key Technologies

- **Language**: Python 3.12+
- **Package Manager**: uv
- **Linter/Formatter**: Ruff
- **Type Checker**: ty
- **Testing**: pytest + Hypothesis
- **Version Management**: Python Semantic Release
- **CI/CD**: GitHub Actions

## Project Layout

This template uses the **src layout** pattern:

- Source code is in `src/python_template/` (rename to `src/your_project_name/`)
- This prevents accidental imports from the project root
- Ensures tests run against the installed package, not the source directory

## Documentation Structure

All detailed documentation is maintained in the `docs/` directory to avoid
duplication and ensure single source of truth:

- 📋 [Requirements Document](./docs/requirements.md) - Project requirements and
    specifications
- 📝 [Conventional Commits](./docs/conventional-commits.md) - Commit message
    format and rules
- Additional documents will be added as needed

## Development Workflow

1. All code changes should be tested
1. Pre-commit hooks will automatically run on commit
1. Follow [Conventional Commits](./docs/conventional-commits.md) format for
    automatic versioning
1. GitHub Actions will handle CI/CD pipeline

## Conventions

- Use double quotes for strings (enforced by Ruff)
- Line length limit: 120 characters
- Follow PEP 8 naming conventions
- Write property-based tests using Hypothesis where applicable

## Notes for Claude

- Always ensure tests are written for new functionality
- Use type hints for all function signatures
- Keep documentation in `docs/` directory updated
- Reference documentation files rather than duplicating content
- Remember to update imports when the package name changes
