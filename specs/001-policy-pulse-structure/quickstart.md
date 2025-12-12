# Quickstart Guide: Policy Pulse Architecture

## Prerequisites

- Python 3.11+ installed
- Node.js 18+ installed
- Windows 10/11 (primary target)
- Git installed
- Basic understanding of Python and JavaScript development

## Installation

### Cloning the Repository

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd policy-pulse
   ```

2. **Verify the directory structure:**
   ```bash
   ls -la
   # Should show:
   # policy-pulse-core/
   # policy-pulse-desktop/
   ```

### Backend Setup (policy-pulse-core)

1. **Navigate to backend directory:**
   ```bash
   cd policy-pulse-core
   ```

2. **Set up Python environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

### Frontend Setup (policy-pulse-desktop)

1. **Navigate to frontend directory:**
   ```bash
   cd ../policy-pulse-desktop
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

## Project Structure Overview

### Backend Structure (`policy-pulse-core/`)
```
policy-pulse-core/
├── src/
│   ├── models/          # Data models and schemas
│   ├── services/        # Business logic and services
│   ├── cli/             # Command-line interface
│   └── lib/             # Shared libraries
├── tests/
│   ├── contract/        # Contract tests
│   ├── integration/     # Integration tests
│   └── unit/            # Unit tests
└── requirements.txt     # Python dependencies
```

### Frontend Structure (`policy-pulse-desktop/`)
```
policy-pulse-desktop/
├── src/
│   ├── components/      # React components
│   ├── main.js          # Electron main process
│   └── preload.js       # Preload script for security
├── public/              # Static assets
├── package.json         # Node.js dependencies and scripts
└── build-windows.bat    # Windows build script
```

## Running the Application

### Backend Services

1. **Start backend services:**
   ```bash
   cd policy-pulse-core
   python -m src.services.main
   ```

2. **Run tests:**
   ```bash
   cd policy-pulse-core
   pytest tests/
   ```

### Frontend Application

1. **Run in development mode:**
   ```bash
   cd policy-pulse-desktop
   npm start
   ```

2. **Build for production:**
   ```bash
   cd policy-pulse-desktop
   npm run build
   ```

3. **Package for Windows:**
   ```bash
   cd policy-pulse-desktop
   build-windows.bat
   ```

## Configuration

### Environment Variables

Set the following environment variables for proper operation:

```bash
# For backend services
export PP_BACKEND_PORT=5000
export PP_LOG_LEVEL=INFO

# For frontend application
export PP_DESKTOP_DEBUG=true
export PP_CONFIG_PATH=./config.json
```

### Configuration Files

The system uses configuration files in JSON format:

**Backend Configuration** (`policy-pulse-core/config.json`):
```json
{
  "server": {
    "port": 5000,
    "host": "localhost"
  },
  "logging": {
    "level": "INFO",
    "file": "app.log"
  }
}
```

**Frontend Configuration** (`policy-pulse-desktop/config.json`):
```json
{
  "window": {
    "width": 1200,
    "height": 800
  },
  "features": {
    "debug": true,
    "auto_update": false
  }
}
```

## Troubleshooting

### Common Issues

1. **Python environment problems:**
   - Ensure you're in the virtual environment
   - Verify Python version is 3.11+

2. **Node.js dependencies issues:**
   - Run `npm install` in the desktop directory
   - Check Node.js version compatibility

3. **Build failures:**
   - Ensure all dependencies are installed
   - Check that build scripts have proper permissions

4. **Cross-platform compatibility:**
   - Windows-specific scripts may not work on other platforms
   - Use the build-windows.bat script for Windows packaging

## Best Practices

1. **Code Organization:**
   - Follow the established directory structure
   - Keep components under 500 lines of code
   - Use descriptive naming conventions

2. **Testing:**
   - Write unit tests for all new components
   - Run integration tests before committing changes
   - Use pytest for Python, Jest for JavaScript

3. **Documentation:**
   - Update documentation when changing architecture
   - Add comments to complex code sections
   - Maintain clear commit messages