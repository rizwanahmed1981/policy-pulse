# Data Model: Policy Pulse Chat Bot

## Core Entities

### PolicyDocument
Represents company policy documents (PDF/DOCX/HTML) containing compliance rules and procedures

**Fields**:
- `id` (UUID): Unique identifier for the document
- `title` (string): Document title
- `source_path` (string): Original location of the document (local/SharePoint/Confluence)
- `content_hash` (string): SHA-256 hash of content for change detection
- `parsed_content` (text): Plain text extracted from the document
- `embedding_vector` (binary): Vector representation of the document content
- `created_at` (datetime): When the document was first processed
- `updated_at` (datetime): When the document was last updated

**Validation**:
- Title must not be empty
- Source path must be valid
- Content hash must be 64 characters (SHA-256)

**Relationships**:
- One-to-many with ComplianceAlert (triggers)

### ChatMessage
Represents messages in Slack/MS Teams channels that may trigger policy guidance responses

**Fields**:
- `id` (string): Platform-specific message ID
- `platform` (enum): 'slack' | 'teams'
- `channel_id` (string): Channel identifier from the platform
- `user_id` (string): User identifier from the platform
- `content` (text): Message content
- `timestamp` (datetime): When the message was posted
- `detected_keywords` (json): Array of detected vendor-related keywords
- `processed` (boolean): Whether the message has been processed by the system

**Validation**:
- Content must not be empty
- Platform must be one of allowed values
- Channel ID must be provided

**Relationships**:
- Zero-to-one with ComplianceAlert (if triggers policy response)

### ComplianceAlert
Represents detected vendor-related discussions that require policy guidance, stored for administrator review

**Fields**:
- `id` (UUID): Unique identifier for the alert
- `chat_message_id` (string): Reference to the triggering chat message
- `policy_matches` (json): Array of matching policy document IDs and relevance scores
- `response_content` (text): The compliance guidance provided to the user
- `triggered_at` (datetime): When the alert was generated
- `reviewed_at` (datetime, nullable): When the alert was reviewed by admin
- `reviewed_by` (string, nullable): User who reviewed the alert
- `escalation_required` (boolean): Whether the alert requires manual review

**Validation**:
- Chat message ID must exist
- Policy matches must contain at least one match
- Triggered at must be set

**Relationships**:
- Many-to-one with ChatMessage (triggers)
- Many-to-many with PolicyDocument (matches)

## State Transitions

### ComplianceAlert States
- `new`: Alert generated, waiting for initial processing
- `processed`: Policy guidance provided, waiting for review
- `reviewed`: Admin has reviewed the alert
- `escalated`: Alert requires additional attention

## Database Schema

```sql
CREATE TABLE policy_documents (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    source_path TEXT NOT NULL,
    content_hash TEXT NOT NULL,
    parsed_content TEXT,
    embedding_vector BLOB,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE chat_messages (
    id TEXT PRIMARY KEY,
    platform TEXT NOT NULL CHECK(platform IN ('slack', 'teams')),
    channel_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    content TEXT NOT NULL,
    timestamp DATETIME NOT NULL,
    detected_keywords JSON,
    processed BOOLEAN DEFAULT FALSE
);

CREATE TABLE compliance_alerts (
    id TEXT PRIMARY KEY,
    chat_message_id TEXT NOT NULL,
    policy_matches JSON NOT NULL,
    response_content TEXT,
    triggered_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    reviewed_at DATETIME,
    reviewed_by TEXT,
    escalation_required BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (chat_message_id) REFERENCES chat_messages(id)
);

CREATE INDEX idx_chat_messages_timestamp ON chat_messages(timestamp);
CREATE INDEX idx_chat_messages_processed ON chat_messages(processed);
CREATE INDEX idx_compliance_alerts_triggered ON compliance_alerts(triggered_at);
```

## API Data Contracts

### Policy Document Upload Request
```json
{
  "title": "string",
  "file_path": "string",
  "source_type": "enum: local|sharepoint|confluence"
}
```

### Chat Message Webhook Payload
```json
{
  "message_id": "string",
  "platform": "enum: slack|teams",
  "channel_id": "string",
  "user_id": "string",
  "content": "string",
  "timestamp": "ISO 8601 datetime"
}
```

### Compliance Alert Response
```json
{
  "alert_id": "UUID",
  "message_content": "string",
  "policy_guidance": [
    {
      "policy_title": "string",
      "relevance_score": "number",
      "guidance_text": "string"
    }
  ],
  "action_checklist": ["string"]
}
```