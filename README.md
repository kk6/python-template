# Python Project Template

A modern Python project template with best practices and tools for development.

## Requirements

- **Claude Code**: This project is designed to work with Claude Code
- **VSCode**: Visual Studio Code is required for development
- **Python 3.12+**: Python 3.12 or higher is required
- **uv**: For dependency management and tool execution

## Features

- 📦 **uv** for fast, reliable Python package management
- 🧹 **Ruff** for linting and formatting
- 🔍 **ty** for type checking
- 🧪 **pytest** for testing with coverage reports
- 🎲 **Hypothesis** for property-based testing
- 🔧 **pre-commit** hooks for code quality
- 📈 **Python Semantic Release** for automated versioning
- 🤖 **GitHub Actions** for CI/CD

## Quick Start

1. **Create a new repository from this template**:

    - Go to the template repository page on GitHub
    - Click "**Use this template**" button
    - Select "**Create a new repository**"
    - Choose repository owner and enter repository name
    - Select visibility (public/private)
    - Click "**Create repository from template**"

1. **Install uv** (if not already installed):

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

1. **Clone your new repository**:

    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

1. **Customize for your project**:

    - Rename `src/python_template/` to `src/your_project_name/`
    - Update `pyproject.toml`:
        - Change `name = "python-template"` to your project name
        - Update `tool.hatch.build.targets.wheel.packages`
        - Update `tool.semantic_release.version_variable`
        - Update `tool.coverage.run.source`
    - Update import statements in tests

1. **Create a virtual environment and install dependencies**:

    ```bash
    uv venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    uv pip install -e ".[dev]"
    ```

1. **Install pre-commit hooks**:

    ```bash
    pre-commit install
    ```

## Development

### Running Tests

```bash
uv run pytest
```

### Running Linter & Formatter

```bash
uv run ruff check --fix .
uv run ruff format .
```

### Running Type Checker

```bash
uv run ty
```

### Manual Pre-commit Run

```bash
pre-commit run --all-files
```

## Project Structure

```text
.
├── src/
│   └── python_template/  # Package source code
│       ├── __init__.py
│       └── example.py
├── tests/                # Test files
├── docs/                 # Documentation
│   └── requirements.md   # Requirements document
├── .github/              # GitHub specific files
│   └── workflows/        # GitHub Actions workflows
├── CLAUDE.md             # Claude-specific documentation
├── README.md             # This file
├── pyproject.toml        # Project configuration
├── .pre-commit-config.yaml  # Pre-commit hooks configuration
└── .gitignore            # Git ignore patterns
```

## Documentation

Project documentation is organized under the `docs/` directory. The
`CLAUDE.md` file serves as an index to these documents rather than duplicating
content.

## Contributing

1. Create a feature branch
1. Make your changes
1. Ensure all tests pass and code is properly formatted
1. Commit your changes (following conventional commit format)
1. Create a pull request

## License

This project is licensed under the MIT License.
