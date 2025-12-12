# Policy Pulse Core

Backend services for Policy Pulse - a micro-compliance bot that provides real-time policy guidance in chat environments.

## Project Structure

```
policy-pulse-core/
├── src/
│   ├── models/          # Data models and schemas
│   ├── services/        # Business logic and services
│   ├── cli/             # Command-line interface
│   └── lib/             # Shared libraries
├── tests/
│   ├── unit/            # Unit tests
│   ├── integration/     # Integration tests
│   └── contract/        # Contract tests
└── requirements.txt     # Python dependencies
```

## Getting Started

1. Install Python 3.11+
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Development

- Backend services use Flask framework
- NLP processing with sentence-transformers
- Document parsing with PyMuPDF and python-docx

## License

MIT License