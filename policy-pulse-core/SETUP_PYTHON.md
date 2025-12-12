# Python Environment Setup

This document explains how to set up the Python environment for Policy Pulse Core.

## Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

## Setup Instructions

### 1. Create Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt
```

### 3. Verify Installation

```bash
# Verify that all dependencies are installed
pip list
```

## Development Workflow

### Activating the Environment

Always activate the virtual environment before working on the project:

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux
```

### Deactivating the Environment

When you're done working:

```bash
deactivate
```

### Adding New Dependencies

When adding new dependencies:

1. Add the dependency to `requirements.txt`
2. Install it in the virtual environment:
   ```bash
   pip install <package-name>
   ```
3. Freeze the requirements:
   ```bash
   pip freeze > requirements.txt
   ```

## Testing

To run tests:

```bash
# Run all tests
pytest tests/

# Run tests with coverage
pytest tests/ --cov=policy_pulse_core
```

## Linting

To check code style:

```bash
# Run flake8
flake8 policy_pulse_core/

# Run black formatting
black policy_pulse_core/
```