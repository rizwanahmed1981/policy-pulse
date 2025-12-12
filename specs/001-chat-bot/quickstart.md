# Quickstart Guide: Policy Pulse Chat Bot

## Prerequisites

- Python 3.11+ installed
- Node.js 18+ installed (for Electron app)
- Windows 10/11 (primary target)
- Administrative access for Windows service installation
- Slack workspace with admin privileges for app installation
- Microsoft Teams tenant with app upload permissions

## Installation

### Backend Service Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd policy-pulse
   ```

2. **Set up Python environment:**
   ```bash
   cd policy-pulse-core
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Install system dependencies:**
   ```bash
   # For PDF parsing
   # On Windows: No additional dependencies needed
   # On Linux: sudo apt-get install poppler-utils
   ```

### Desktop Application Setup

1. **Navigate to desktop directory:**
   ```bash
   cd policy-pulse-desktop
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

## Configuration

### Slack Integration

1. **Create a Slack App:**
   - Go to https://api.slack.com/apps
   - Click "Create New App"
   - Select "From scratch"
   - Name your app (e.g., "Policy Pulse")
   - Select your workspace

2. **Configure Bot Token Scopes:**
   - Go to "OAuth & Permissions"
   - Add scopes: `chat:write`, `channels:history`, `groups:history`, `im:history`, `mpim:history`

3. **Enable Event Subscriptions:**
   - Go to "Event Subscriptions"
   - Enable events
   - Add Request URL: `https://<your-domain>/api/slack/events`
   - Subscribe to bot events: `message.channels`, `message.groups`, `message.im`, `message.mpim`

### Microsoft Teams Integration

1. **Create Teams App:**
   - Go to https://dev.teams.microsoft.com/apps
   - Create new app
   - Configure as bot with messaging endpoint: `https://<your-domain>/api/teams/webhook`

2. **Configure permissions:**
   - Add required permissions for reading chat messages
   - Configure for side-loading in your tenant

## Running the Application

### Backend Service

1. **Start the core service:**
   ```bash
   cd policy-pulse-core
   python -m src.api.chat_webhooks
   ```

2. **Install as Windows service (optional):**
   ```bash
   python -m src.services.windows_service install
   python -m src.services.windows_service start
   ```

### Desktop Application

1. **Run in development mode:**
   ```bash
   cd policy-pulse-desktop
   npm start
   ```

2. **Build for production:**
   ```bash
   npm run build
   npm run package
   ```

## Initial Setup

1. **Upload policy documents:**
   - Open the desktop application
   - Navigate to "Documents" section
   - Upload your organization's policy documents (PDF, DOCX, HTML)

2. **Configure monitored channels:**
   - In the desktop app, go to "Settings"
   - Add channel IDs for Slack/Teams that should be monitored
   - Set up vendor-related keywords to watch for

3. **Test the integration:**
   - Post a test message in a monitored channel containing vendor keywords
   - Verify that the bot responds with relevant policy guidance

## Security Configuration

### Database Encryption

1. **Set up encryption password:**
   ```bash
   # Set environment variable
   export PP_ENCRYPTION_KEY="your-secure-password"
   ```

2. **The system will automatically encrypt the local database using AES-256**

## Troubleshooting

### Common Issues

1. **Bot not responding in channels:**
   - Verify the bot has been added to the specific channels
   - Check webhook URLs are accessible from Slack/Teams
   - Review application logs

2. **Document parsing failures:**
   - Ensure documents are not password-protected
   - Check file size limits (recommended <10MB per document)
   - Verify supported formats (PDF, DOCX, HTML)

3. **Performance issues:**
   - Monitor memory usage (should stay under 150MB)
   - Check vector database size
   - Consider indexing strategy for large document sets