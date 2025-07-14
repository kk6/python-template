# Testing Guide

This guide covers testing practices, tools, and patterns used in this project.

## Testing Framework

### pytest

This project uses pytest as the primary testing framework with the following features:

- Automatic test discovery
- Fixtures for setup and teardown
- Parametrized tests
- Coverage reporting
- Integration with CI/CD

### Key Configuration

See `pyproject.toml` for pytest configuration:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = [
    "--cov=src",
    "--cov-report=term-missing",
    "--cov-report=html",
    "--cov-report=xml",
    "-v",
]
```

## Test Structure

### Directory Layout

```text
tests/
├── __init__.py
├── test_example.py
├── unit/
│   ├── test_module1.py
│   └── test_module2.py
├── integration/
│   └── test_integration.py
└── fixtures/
    └── conftest.py
```

### Test Organization

- **Unit tests**: Test individual functions and classes
- **Integration tests**: Test component interactions
- **Fixtures**: Reusable test data and setup

## Writing Tests

### Test-Driven Development (TDD)

Follow the TDD cycle:

1. **Red**: Write a failing test
1. **Green**: Write minimal code to pass
1. **Refactor**: Improve code while keeping tests passing

### AAA Pattern

Structure tests using Arrange-Act-Assert:

```python
def test_calculate_total():
    # Arrange
    items = [10, 20, 30]
    expected = 60

    # Act
    result = calculate_total(items)

    # Assert
    assert result == expected
```

### Test Naming

Use descriptive names that explain what is being tested:

```python
def test_user_login_with_valid_credentials():
    """Test that user can login with valid username and password."""
    # Test implementation

def test_user_login_fails_with_invalid_password():
    """Test that login fails when password is incorrect."""
    # Test implementation
```

## Testing Patterns

### Fixtures

Use fixtures for reusable test data:

```python
import pytest

@pytest.fixture
def sample_user():
    """Create a sample user for testing."""
    return {
        "id": 1,
        "name": "Test User",
        "email": "test@example.com"
    }

def test_user_creation(sample_user):
    """Test user object creation."""
    user = User(**sample_user)
    assert user.name == "Test User"
```

### Parametrized Tests

Test multiple inputs with parametrization:

```python
@pytest.mark.parametrize("input_value,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
    (0, 0),
])
def test_double_function(input_value, expected):
    """Test double function with various inputs."""
    assert double(input_value) == expected
```

### Exception Testing

Test that functions raise appropriate exceptions:

```python
def test_divide_by_zero_raises_error():
    """Test that dividing by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
```

## Property-Based Testing with Hypothesis

### Basic Usage

Use Hypothesis for property-based testing:

```python
from hypothesis import given, strategies as st

@given(st.integers(), st.integers())
def test_addition_commutative(a, b):
    """Test that addition is commutative."""
    assert add(a, b) == add(b, a)

@given(st.lists(st.integers()))
def test_reverse_twice_is_identity(lst):
    """Test that reversing a list twice gives the original."""
    assert reverse(reverse(lst)) == lst
```

### Custom Strategies

Create custom strategies for domain objects:

```python
from hypothesis import strategies as st

@st.composite
def user_strategy(draw):
    """Generate valid user objects."""
    name = draw(st.text(min_size=1, max_size=50))
    email = draw(st.emails())
    age = draw(st.integers(min_value=0, max_value=150))
    return User(name=name, email=email, age=age)

@given(user_strategy())
def test_user_serialization(user):
    """Test user serialization roundtrip."""
    data = user.to_dict()
    restored = User.from_dict(data)
    assert restored == user
```

## Test Coverage

### Coverage Goals

- Maintain overall coverage above 80%
- Critical paths should have 100% coverage
- New features must include tests

### Running Coverage

```bash
# Run tests with coverage
pytest --cov

# Generate HTML report
pytest --cov --cov-report=html

# View coverage report
open htmlcov/index.html
```

### Coverage Configuration

See `pyproject.toml` for coverage settings:

```toml
[tool.coverage.run]
source = ["src"]
omit = ["*/tests/*", "*/__init__.py"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if __name__ == .__main__.:",
    "raise NotImplementedError",
]
```

## Mocking and Patching

### Using unittest.mock

```python
from unittest.mock import Mock, patch

def test_external_api_call():
    """Test function that calls external API."""
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {"status": "success"}

        result = fetch_data_from_api()

        assert result["status"] == "success"
        mock_get.assert_called_once()
```

### pytest-mock

```python
def test_database_query(mocker):
    """Test database query with mocked connection."""
    mock_db = mocker.patch('app.database.connect')
    mock_db.return_value.query.return_value = [{"id": 1, "name": "test"}]

    result = get_user_by_id(1)

    assert result["name"] == "test"
```

## Integration Testing

### Database Testing

```python
@pytest.fixture
def test_db():
    """Create test database for integration tests."""
    db = create_test_database()
    yield db
    db.cleanup()

def test_user_crud_operations(test_db):
    """Test complete user CRUD operations."""
    # Create
    user = create_user(test_db, "test@example.com")
    assert user.id is not None

    # Read
    retrieved = get_user(test_db, user.id)
    assert retrieved.email == "test@example.com"

    # Update
    update_user(test_db, user.id, {"name": "Updated Name"})
    updated = get_user(test_db, user.id)
    assert updated.name == "Updated Name"

    # Delete
    delete_user(test_db, user.id)
    assert get_user(test_db, user.id) is None
```

### API Testing

```python
def test_api_endpoint(client):
    """Test API endpoint response."""
    response = client.post("/api/users", json={
        "name": "Test User",
        "email": "test@example.com"
    })

    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"
```

## Performance Testing

### Basic Performance Tests

```python
import time
import pytest

def test_function_performance():
    """Test that function completes within time limit."""
    start = time.time()

    result = expensive_function(large_dataset)

    duration = time.time() - start
    assert duration < 1.0  # Should complete in under 1 second
    assert result is not None
```

### Memory Usage Testing

```python
import psutil
import os

def test_memory_usage():
    """Test that function doesn't use excessive memory."""
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss

    result = memory_intensive_function()

    final_memory = process.memory_info().rss
    memory_increase = final_memory - initial_memory

    # Should not increase memory by more than 100MB
    assert memory_increase < 100 * 1024 * 1024
```

## Running Tests

### Local Testing

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_example.py

# Run with coverage
pytest --cov

# Run in verbose mode
pytest -v

# Run only failed tests
pytest --lf

# Run tests matching pattern
pytest -k "test_user"
```

### CI/CD Integration

Tests run automatically on:

- Every commit (pre-commit hooks)
- Pull requests (GitHub Actions)
- Main branch updates

## Test Data Management

### Fixtures and Factories

```python
@pytest.fixture
def user_factory():
    """Factory for creating test users."""
    def _create_user(**kwargs):
        defaults = {
            "name": "Test User",
            "email": "test@example.com",
            "active": True
        }
        defaults.update(kwargs)
        return User(**defaults)
    return _create_user

def test_user_activation(user_factory):
    """Test user activation functionality."""
    user = user_factory(active=False)
    user.activate()
    assert user.active is True
```

### Test Database Setup

```python
@pytest.fixture(scope="session")
def test_database():
    """Create test database for entire test session."""
    db = create_test_database()
    setup_test_schema(db)
    yield db
    db.drop_all_tables()
    db.close()
```

## Best Practices

### General Guidelines

1. **Test behavior, not implementation**
1. **Keep tests simple and focused**
1. **Use descriptive test names**
1. **Test edge cases and error conditions**
1. **Maintain test independence**

### Code Quality

- Follow same code style as main code
- Use type hints in test functions
- Keep test functions short and focused
- Avoid complex logic in tests

### Performance

- Use appropriate test scope (function, class, module, session)
- Mock external dependencies
- Use fixtures for expensive setup
- Parallelize tests when possible

## Debugging Tests

### Common Issues

1. **Flaky tests**: Use proper fixtures and avoid time-dependent tests
1. **Slow tests**: Profile and optimize or use mocking
1. **Hard to maintain**: Keep tests simple and well-organized

### Debugging Tools

```bash
# Run with debugging
pytest --pdb

# Run with print statements
pytest -s

# Run single test with debugging
pytest tests/test_example.py::test_function -v -s
```

## Resources

- [pytest documentation](https://docs.pytest.org/)
- [Hypothesis documentation](https://hypothesis.readthedocs.io/)
- [Testing best practices](https://docs.python.org/3/library/unittest.html)
- [Coverage.py documentation](https://coverage.readthedocs.io/)
