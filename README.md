# Python Project Template

A modern Python project template with best practices and tools for development.

## Requirements

- **Claude Code**: This project is designed to work with Claude Code
- **VSCode**: Visual Studio Code is required for development
- **mise**: For Python version and tool management
- **Python 3.12+**: Python 3.12 or higher (managed by mise)
- **uv**: For dependency management and tool execution (managed by mise)

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

1. **Install mise** (if not already installed):

    ```bash
    curl https://mise.jdx.dev/install.sh | sh
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

1. **Install tools and dependencies**:

    ```bash
    mise install  # Installs Python 3.12 and uv, creates virtual environment
    uv sync       # Install dependencies and create virtual environment
    ```

1. **Install pre-commit hooks**:

    ```bash
    pre-commit install
    ```

1. **Setup Semantic Release (for automated versioning)**:

    After creating your project from this template, follow these steps to
    enable automated releases:

    - Rename `.github/workflows/release.yml.example` to
        `.github/workflows/release.yml`
    - Verify the version setting in `pyproject.toml` is set to your desired
        initial version (default: `0.0.0`)
    - Commit and push your first changes using
        [Conventional Commits](./docs/conventional-commits.md) format
    - Your first release will be automatically created when you push to the
        main branch

For more detailed documentation, see [Development Environment Setup](./docs/development-setup.md).

## Development

### Running Tests

```bash
mise run test
```

### Running Linter & Formatter

```bash
mise run lint       # Check for linting issues
mise run format     # Format code
mise run fix        # Fix linting issues
```

### Running Type Checker

```bash
mise run typecheck
```

### Running All Checks

```bash
mise run check      # Run tests, linting, and type checking
```

### Fix and Check

```bash
mise run fix-and-check  # Fix issues, format, and run all checks
```

### Additional Commands

```bash
pre-commit run --all-files  # Run pre-commit hooks manually
mise run clean              # Clean build artifacts and cache
```

For more detailed documentation, see [mise Tasks](./docs/mise-tasks.md).

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
├── .mise.toml            # mise configuration for Python and tool management
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
