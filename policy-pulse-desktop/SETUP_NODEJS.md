# Node.js Environment Setup

This document explains how to set up the Node.js environment for Policy Pulse Desktop.

## Prerequisites

- Node.js 18 or higher
- npm (Node package manager)

## Setup Instructions

### 1. Install Dependencies

```bash
# Install project dependencies
npm install
```

### 2. Verify Installation

```bash
# Check that dependencies are installed
npm list
```

## Development Workflow

### Running the Application

```bash
# Run in development mode
npm start

# Build for production
npm run build

# Run tests
npm test
```

### Adding New Dependencies

When adding new dependencies:

```bash
# Add a production dependency
npm install <package-name>

# Add a development dependency
npm install --save-dev <package-name>
```

### Managing Dependencies

```bash
# Update all dependencies
npm update

# Remove a dependency
npm uninstall <package-name>
```

## Scripts

The project includes the following npm scripts:

- `npm start` - Run the application in development mode
- `npm run build` - Build the application for production
- `npm test` - Run tests
- `npm run test:watch` - Run tests in watch mode

## Testing

To run tests:

```bash
# Run all tests
npm test

# Run tests with coverage
npm run test:coverage
```

## Linting

To check code style:

```bash
# Run ESLint
npm run lint

# Run Prettier
npm run format
```

## Environment Variables

Create a `.env` file in the project root for environment-specific configuration:

```bash
# Example .env file
NODE_ENV=development
APP_NAME=Policy Pulse
```

## Troubleshooting

### Common Issues

1. **Permission errors**:
   ```bash
   # Fix permissions on node_modules
   sudo chown -R $(whoami) node_modules
   ```

2. **Outdated dependencies**:
   ```bash
   # Update npm
   npm install -g npm@latest
   ```

3. **Missing dependencies**:
   ```bash
   # Reinstall all dependencies
   rm -rf node_modules package-lock.json
   npm install
   ```