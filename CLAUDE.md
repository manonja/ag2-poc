# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Structure

This is a modern Python package using:
- **uv** for dependency management and virtual environments
- **Pydantic** for data validation and settings
- **mypy** with strict type checking
- **pytest** for testing

## Essential Commands

### Environment Setup
```bash
# Install dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate  # or `uv shell`
```

### Development Commands
```bash
# Run type checking (strict mode)
uv run mypy src/

# Run linting
uv run ruff check src/
uv run ruff format src/

# Run tests
uv run pytest

# Run specific test
uv run pytest tests/test_specific.py::test_function

# Run tests with coverage
uv run pytest --cov=src/
```

### Building and Installation
```bash
# Build package
uv build

# Install in development mode
uv pip install -e .
```

## Code Standards

### Type Checking
- All code must pass mypy strict mode
- Use explicit type annotations for all function parameters and return values
- Avoid `Any` types unless absolutely necessary

### Pydantic Models
- Use Pydantic v2 syntax
- Define models in `src/models/` directory
- Use `BaseModel` for data structures
- Use `BaseSettings` for configuration

### Commit Convention
- Follow conventional commits: `type(scope): description`
- Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- No emojis in commit messages
- No "Co-authored-by: Claude" in commits

## Project Architecture

```
src/
├── __init__.py          # Package initialization
├── models/              # Pydantic models and schemas
├── core/                # Core business logic
├── utils/               # Utility functions
└── config.py            # Configuration using Pydantic Settings

tests/
├── __init__.py
├── test_models/         # Model tests
├── test_core/           # Core logic tests
└── conftest.py          # Pytest configuration
```

## Configuration Files

- `pyproject.toml` - Project metadata, dependencies, and tool configuration
- `uv.lock` - Locked dependency versions (commit this file)
- `mypy.ini` or `pyproject.toml` - mypy strict configuration
- `.gitignore` - Standard Python gitignore with uv-specific entries