# Conventional Commits

This project follows the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
specification for commit messages.

## Format

```text
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## Type

The type must be one of the following:

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code (white-space,
    formatting, missing semi-colons, etc)
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **perf**: A code change that improves performance
- **test**: Adding missing tests or correcting existing tests
- **build**: Changes that affect the build system or external dependencies
- **ci**: Changes to CI configuration files and scripts
- **chore**: Other changes that don't modify src or test files
- **revert**: Reverts a previous commit

## Scope

The scope is optional and should be a noun describing a section of the
codebase surrounded by parentheses, e.g., `feat(parser): add ability to parse arrays`.

## Description

The description is a short summary of the code change:

- Use the imperative, present tense: "change" not "changed" nor "changes"
- Don't capitalize the first letter
- No dot (.) at the end

## Body

The body is optional and should include the motivation for the change and
contrast this with previous behavior.

## Footer

The footer is optional and should contain any information about **Breaking
Changes** and is also the place to reference GitHub issues that this commit
**Closes**.

## Examples

### Feature

```text
feat(lang): add Japanese language support
```

### Bug Fix

```text
fix(user): prevent racing of requests

Introduce a request id and a reference to latest request. Dismiss
incoming responses other than from latest request.

Remove timeouts which were used to mitigate the racing issue but are
obsolete now.

Fixes #123
```

### Breaking Change

```text
feat(api): remove deprecated endpoints

BREAKING CHANGE: The /api/v1/users endpoint has been removed.
Use /api/v2/users instead.
```

### Scope Examples for This Project

- `feat(parser)`: Changes to parsing functionality
- `fix(auth)`: Authentication related fixes
- `docs(readme)`: README documentation changes
- `test(unit)`: Unit test changes
- `build(deps)`: Dependency updates
- `ci(github)`: GitHub Actions workflow changes

## Benefits

Following Conventional Commits:

1. **Automatically generates** CHANGELOGs
1. **Automatically determines** semantic version bump
1. **Triggers** build and publish processes
1. **Makes it easier** for people to contribute by allowing them to explore a
    more structured commit history
1. **Communicates** the nature of changes to teammates and the public

## Integration with Python Semantic Release

This project uses [Python Semantic Release](https://python-semantic-release.readthedocs.io/)
which automatically:

- Analyzes commit messages
- Determines the next version number
- Generates changelog
- Creates Git tags
- Publishes releases

### Version Bump Rules

- `fix:` → patch version (0.0.1)
- `feat:` → minor version (0.1.0)
- `BREAKING CHANGE:` → major version (1.0.0)

## Tools and Validation

- **Pre-commit hooks**: Automatically validate commit message format
- **GitHub Actions**: CI pipeline validates commit messages
- **Semantic Release**: Processes commits for automatic versioning
