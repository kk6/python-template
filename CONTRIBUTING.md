# Contributing Guidelines

Thank you for your interest in contributing to this project! This guide will
help you get started with contributing effectively.

## Development Setup

1. **Fork and Clone**

    ```bash
    git clone <your-fork-url>
    cd py-template
    ```

1. **Install Dependencies**

    ```bash
    uv sync
    source .venv/bin/activate  # or `.venv\Scripts\activate` on Windows
    ```

1. **Install Pre-commit Hooks**

    ```bash
    pre-commit install
    ```

1. **Verify Setup**

    ```bash
    pytest  # Run tests
    ruff check  # Check linting
    ty check  # Run type checking
    ```

For detailed setup instructions, see [Development Setup Guide](./docs/development-setup.md).

## Development Workflow

### Test-Driven Development (TDD)

This project follows TDD principles:

1. **Red**: Write a failing test
1. **Green**: Write minimal code to make it pass
1. **Refactor**: Improve code while keeping tests passing

### Branch Strategy

1. Create a new branch from `main`:

    ```bash
    git checkout -b feature/your-feature-name
    ```

1. Use descriptive branch names:

    - `feature/add-user-authentication`
    - `fix/handle-empty-input`
    - `docs/update-api-documentation`

### During Development

1. **Write Tests First**: Follow TDD practices

1. **Run Tests Frequently**: `pytest`

1. **Check Code Quality**:

    ```bash
    ruff check --fix  # Auto-fix issues
    ruff format       # Format code
    ty check          # Type checking
    ```

1. **Update Documentation**: Keep docs current

### Commit Guidelines

We use [Conventional Commits](https://www.conventionalcommits.org/) for
automatic versioning:

**Format:**

```text
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or modifying tests
- `chore`: Maintenance tasks

**Examples:**

```text
feat(auth): add user login functionality
fix(parser): handle empty input gracefully
docs(api): update authentication endpoints
test(utils): add tests for string utilities
```

### Pull Request Process

1. **Before Creating PR**:

    - Ensure all tests pass
    - Check that code is properly formatted
    - Update documentation if needed
    - Rebase on latest main

1. **Create Pull Request**:

    - Use descriptive title and description
    - Link to relevant issues
    - Add screenshots for UI changes
    - Include testing instructions

1. **After Review**:

    - Address feedback promptly
    - Keep commits clean and focused
    - Update PR description if scope changes

## Code Quality Standards

### Code Style

- Follow PEP 8 conventions
- Use type hints for all function signatures
- Write Google-style docstrings
- Maximum line length: 120 characters
- Use double quotes for strings

### Example Function

```python
def calculate_total(items: List[Dict[str, Any]]) -> Dict[str, float]:
    """Calculate total price and tax for a list of items.

    Args:
        items: List of item dictionaries with 'price' and 'tax_rate' keys

    Returns:
        Dictionary with 'subtotal', 'tax', and 'total' keys

    Raises:
        ValueError: If items list is empty or contains invalid data
    """
    if not items:
        raise ValueError("Items list cannot be empty")

    subtotal = sum(item["price"] for item in items)
    tax = sum(item["price"] * item["tax_rate"] for item in items)

    return {
        "subtotal": subtotal,
        "tax": tax,
        "total": subtotal + tax
    }
```

## Testing Requirements

### Test Coverage

- Maintain overall coverage above 80%
- Write tests for new features
- Update tests when modifying existing code

### Test Types

- **Unit Tests**: Test individual functions and classes
- **Integration Tests**: Test component interactions
- **Property-Based Tests**: Use Hypothesis for edge cases

### Test Example

```python
from hypothesis import given, strategies as st

def test_calculate_total_basic():
    """Test basic total calculation."""
    # Arrange
    items = [
        {"price": 10.0, "tax_rate": 0.1},
        {"price": 20.0, "tax_rate": 0.1}
    ]

    # Act
    result = calculate_total(items)

    # Assert
    assert result["subtotal"] == 30.0
    assert result["tax"] == 3.0
    assert result["total"] == 33.0

@given(st.lists(st.dictionaries(
    keys=st.just("price") | st.just("tax_rate"),
    values=st.floats(min_value=0, max_value=1000)
), min_size=1))
def test_calculate_total_property(items):
    """Test total calculation properties."""
    result = calculate_total(items)
    assert result["total"] == result["subtotal"] + result["tax"]
```

For detailed testing information, see [Testing Guide](./docs/testing.md).

## Documentation

### Documentation Structure

- Keep detailed docs in `docs/` directory
- Update README.md for user-facing changes
- Reference docs from other files rather than duplicating

### Available Documentation

- [Development Setup](./docs/development-setup.md)
- [Testing Guide](./docs/testing.md)
- [Requirements Document](./docs/requirements.md)
- [API Documentation](./docs/api.md)

### Documentation Standards

- Use clear, concise language
- Include code examples
- Keep content up to date
- Use proper markdown formatting

## Release Process

### Versioning

- Uses semantic versioning (SemVer)
- Automated through semantic-release
- Based on conventional commit messages

### Automated Releases

The release process is fully automated using semantic-release with uv integration:

**Version Bumps:**

- `feat`: Minor version bump (0.1.0 → 0.2.0)
- `fix`: Patch version bump (0.1.0 → 0.1.1)
- `BREAKING CHANGE`: Major version bump (0.1.0 → 1.0.0)

**Release Process:**

1. Version updated in `pyproject.toml` and source code
1. `uv.lock` file automatically updated and committed
1. Package built using uv
1. Git tag created and GitHub release published

No manual intervention required for lock file management.

## Getting Help

### Resources

- [Development Setup Guide](./docs/development-setup.md)
- [Testing Guide](./docs/testing.md)
- [Requirements Document](./docs/requirements.md)

### Support Channels

- GitHub Issues: For bugs and feature requests
- GitHub Discussions: For questions and general discussion
- Code Review: For implementation guidance

## Code of Conduct

- Be respectful and constructive
- Follow the project's coding standards
- Help maintain a welcoming environment
- Focus on the code, not the person

## Questions?

Feel free to open an issue or start a discussion if you have any questions or concerns!
