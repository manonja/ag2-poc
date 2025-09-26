# Receipt Scanner AG2

A Python-based receipt scanner application using the AG2 framework.

## Requirements

- Python 3.12+
- uv (for dependency management)

## Local Setup

```bash
# Clone the repository
git clone <repository-url>
cd receipt-scanner-ag2

# Install dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate  # or use `uv shell`

# Run the application
python src/main.py
```

## Development

```bash
# Run type checking
uv run mypy src/

# Run tests
uv run pytest

# Lint code
uv run ruff check src/
```