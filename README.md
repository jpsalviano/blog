# Blog API

A FastAPI-based backend API for a blog platform.

## Features

- 🚀 Modern Python with FastAPI
- 🔒 Environment-based configuration
- ✅ Comprehensive test suite
- 🧹 Code quality enforcement with Ruff
- 📦 Dependency management with uv

## Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) - A modern Python package manager

## Setup and Installation

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/blog-api.git
   cd blog-api
   ```

2. Set up environment variables
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

3. Create a virtual environment and install dependencies
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -e ".[dev,test]"
   ```

## Development

### Running the application

```bash
python -m src.main
```

Or with uvicorn directly:
```bash
uvicorn src.main:app --reload
```

### Running tests

```bash
uv run pytest
```

or if you've set up taskipy in your pyproject.toml:

```bash
uv run task test
```

### Code quality

We use Ruff for linting and formatting. Run before committing:

```bash
uv run ruff check .
uv run ruff format .
```

## Project Structure

```
.
├── .env.example            # Template for environment variables
├── .gitignore              # Git ignore file
├── README.md               # Project documentation
├── pyproject.toml          # Project configuration
├── src/                    # Source code
│   ├── __init__.py
│   ├── config.py           # Configuration management
│   ├── main.py             # Application entry point
└── tests/                  # Test suite
    ├── __init__.py
    ├── conftest.py         # Test configuration
    └── test_health.py      # Health endpoint tests
```

## Branching Strategy

- `main` - Protected branch for production-ready code
- `feature/*` - Feature branches for development

## Contributing

1. Create a new feature branch (`git checkout -b feature/your-feature`)
2. Write tests for your feature
3. Implement your feature
4. Ensure tests pass (`uv run task test`)
5. Format and lint your code (`uv run ruff check . && uv run ruff format .`)
6. Commit your changes with a descriptive message
7. Open a pull request to `main`

## License

[MIT](LICENSE)
