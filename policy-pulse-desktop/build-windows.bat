@echo off
echo Building Policy Pulse for Windows...

REM Install dependencies if not already installed
if not exist node_modules (
    echo Installing Node.js dependencies...
    npm install
)

REM Build the application
echo Building Electron application...
npm run build

echo Build complete!
echo Output files are in the 'dist' folder
pause