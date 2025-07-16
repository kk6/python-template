# mise Tasks

This project leverages [mise](https://mise.jdx.dev/) task functionality to
streamline development tasks.

## Available Tasks

### Basic Tasks

```bash
# Run tests
mise run test

# Run linting
mise run lint

# Format code
mise run format

# Type checking
mise run typecheck

# Run all checks (test, lint, typecheck)
mise run check
```

### Fix and Check

```bash
# Auto-fix lint issues
mise run fix

# Fix and then run all checks
mise run fix-and-check
```

### Maintenance Tasks

```bash
# Clean build artifacts and cache
mise run clean
```

## Task Features

### Parallel Execution

`mise run check` runs dependent tasks (test, lint, typecheck) in parallel.

### Short Forms

Short forms are available when they don't conflict with commands:

```bash
mise test    # Same as mise run test
mise lint    # Same as mise run lint
mise format  # Same as mise run format
```

### Environment Variables

Each task automatically sets the following environment variables:

- `MISE_ORIGINAL_CWD`: Original working directory
- `MISE_CONFIG_ROOT`: Directory containing `.mise.toml`
- `MISE_PROJECT_ROOT`: Project root
- `MISE_TASK_NAME`: Name of the running task

## CI/CD Integration

You can run the same commands locally as in GitHub Actions:

```bash
# Run the same checks as CI environment (no code changes)
mise run check
```

## Usage Guidelines

### During Development

- `mise run fix-and-check` - Fix issues then run all checks
- `mise run format` - Code formatting only

### CI/CD Environment

- `mise run check` - Pure checks (no code changes)

### Individual Verification

- `mise run test` - Tests only
- `mise run lint` - Linting only
- `mise run typecheck` - Type checking only

## Adding Custom Tasks

To add new tasks, add them to the `[tasks]` section in `.mise.toml`:

```toml
[tasks.my-task]
description = "My custom task"
run = "echo 'Hello, World!'"
depends = ["test"]  # Dependencies (optional)
```

## Troubleshooting

### When Tasks Are Not Found

```bash
mise tasks  # Check available tasks
```

### Python Environment Issues

```bash
mise install  # Re-setup Python environment
```

### Verbose Logging

```bash
mise run --verbose test  # Verbose log output
```

## Reference Information

- [mise Tasks Documentation](https://mise.jdx.dev/tasks/)
- [mise Configuration](https://mise.jdx.dev/configuration.html)
