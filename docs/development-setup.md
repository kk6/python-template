# Development Environment Setup

This guide will help you set up your development environment for this Python
project template.

## Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) package manager
- [Git](https://git-scm.com/) for version control

## Quick Start

1. **Clone the repository**

    ```bash
    git clone <repository-url>
    cd py-template
    ```

1. **Install dependencies**

    ```bash
    uv sync
    ```

1. **Activate the virtual environment**

    ```bash
    source .venv/bin/activate
    ```

1. **Install pre-commit hooks**

    ```bash
    pre-commit install
    ```

1. **Run tests to verify setup**

    ```bash
    pytest
    ```

## Development Tools

### Package Management with uv

This project uses `uv` for fast Python package management:

- **Install dependencies**: `uv sync`
- **Add new dependency**: `uv add <package-name>`
- **Add development dependency**: `uv add --dev <package-name>`
- **Update dependencies**: `uv sync --upgrade`

### Code Quality Tools

#### Ruff (Linting and Formatting)

- **Lint code**: `ruff check`
- **Format code**: `ruff format`
- **Fix auto-fixable issues**: `ruff check --fix`

#### Type Checking with ty

- **Run type checking**: `ty`
- **Configuration**: See `[tool.ty.environment]` in `pyproject.toml`

#### Pre-commit Hooks

Pre-commit hooks automatically run on each commit:

- Code formatting with Ruff
- Type checking with ty
- Basic Git hooks

### Testing

#### Running Tests

- **All tests**: `pytest`
- **With coverage**: `pytest --cov`
- **Watch mode**: `pytest --watch` (if pytest-watch is installed)

#### Test Structure

- Unit tests in `tests/` directory
- Use pytest fixtures for setup
- Property-based testing with Hypothesis
- Coverage reports generated in `htmlcov/`

## IDE Setup

### VSCode

The project includes VSCode configuration for optimal development experience:

- **Extensions**: Python, Ruff, Pylance
- **Settings**: Configured for this project's code style
- **Debugging**: Launch configurations included

### Claude Code

This project is optimized for Claude Code integration:

- **CLAUDE.md**: Contains project-specific instructions
- **Documentation**: Structured for easy reference
- **Workflows**: Follows TDD and conventional commits

## Configuration Files

### pyproject.toml

Central configuration file containing:

- Project metadata
- Dependencies
- Tool configurations (Ruff, pytest, coverage, etc.)
- Build system settings

### Key Configuration Sections

- **[tool.ruff]**: Linting and formatting rules
- **[tool.pytest.ini_options]**: Test configuration
- **[tool.coverage]**: Coverage reporting settings
- **[tool.semantic_release]**: Version management with uv integration

### Version Management

The project uses semantic-release with uv integration for automated versioning:

- **Automatic versioning**: Based on conventional commit messages
- **Lock file management**: `uv.lock` is automatically updated during releases
- **Build integration**: Uses uv for building packages during release process

Release process automatically:

1. Updates package version in `pyproject.toml`
1. Updates `__version__` in source code
1. Updates and commits `uv.lock` file
1. Builds package using uv
1. Creates git tag and release

## Common Commands

| Task                 | Command                      |
| -------------------- | ---------------------------- |
| Install dependencies | `uv sync`                    |
| Run tests            | `pytest`                     |
| Format code          | `ruff format`                |
| Lint code            | `ruff check`                 |
| Type check           | `ty`                         |
| Run all checks       | `pre-commit run --all-files` |

## Troubleshooting

### Common Issues

1. **Virtual environment not activated**

    - Solution: `source .venv/bin/activate`

1. **Dependencies not found**

    - Solution: `uv sync` to install all dependencies

1. **Pre-commit hooks failing**

    - Solution: Fix the issues shown or use `git commit --no-verify` (not recommended)

1. **Type checking errors**

    - Solution: Add type hints or use `# type: ignore` comments

### Getting Help

- Check the [Contributing Guide](./contributing.md) for development workflows
- Review the [Testing Guide](./testing.md) for testing best practices
- See the [Requirements Document](./requirements.md) for project specifications
