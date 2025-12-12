# Policy Pulse Desktop

Windows desktop application for Policy Pulse - a micro-compliance bot that provides real-time policy guidance in chat environments.

## Project Structure

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

## Getting Started

1. Install Node.js 18+
2. Install dependencies:
   ```bash
   npm install
   ```

## Development

- Desktop application built with Electron
- UI components built with React
- Windows-native support with Windows-specific build scripts

## License

MIT License