# CPU Dispatch Algorithm Tester - Requirements

This directory contains dependency specifications for the project.

## Files

### `base.txt`
Production dependencies (currently empty - no external dependencies required).

### `dev.txt`
Development and testing dependencies (optional tools for code quality).

## Modern Alternative: pyproject.toml

This project uses `pyproject.toml` (PEP 517/518) which is the modern Python packaging standard and provides:

✅ Project metadata
✅ Python version requirements
✅ Optional dependencies (dev, test)
✅ Tool configurations (black, isort, pytest)
✅ Single source of truth for package information

## Installation

### Standard Installation
```bash
python3 -m pip install -e .
```

### With Development Tools (future use)
```bash
python3 -m pip install -e ".[dev]"
```

### With Test Tools (future use)
```bash
python3 -m pip install -e ".[test]"
```

## No External Dependencies

This project uses only Python standard library modules:
- `collections` - deque for queue operations
- `typing` - type hints
- `sys` - system operations
- `pathlib` - modern file path handling

This means you can run the entire project with just Python 3.6+!
