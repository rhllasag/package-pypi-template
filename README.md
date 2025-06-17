

# Python Package Template

This repository provides a recommended structure for creating and distributing a Python package.

## Requirements

- **Python 3.8 or higher**

## Setup

1. Upgrade pip and install build tools:

    ```bash
    pip install --upgrade pip
    pip install --upgrade build
    ```

## Customization

- Rename the folder `rhllasag-package` to your desired package name.
- Update and customize functions in `__main__.py`.
- Edit `pyproject.toml` with your package details:
    - `name`
    - `version`
    - `author`
    - `python_requires`

## Building the Package

Build your package locally:

```bash
python -m build
```

This command creates a `/dist` directory containing your package distributions.

## Local Installation

Install your package in your local environment:

```bash
pip install .\dist\<your-package-name\>-<version>.tar.gz
```

Replace `<your-package-name>` and `<version>` with your actual package name and version.

## Publishing to PyPI

Upload your package to PyPI using Twine:

```bash
twine upload dist/*
```

After uploading, verify the package is available in your PyPI account.

## Usage Example

Import and use your package in Python code:

```python
import rhllasag_package

rhllasag_package.main()
```
