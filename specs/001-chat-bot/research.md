# Research: Policy Pulse Chat Bot

## Phase 0: Technical Research and Decision Log

### Decision: Technology Stack
**Rationale**: Selected Python for backend services due to strong NLP/ML ecosystem (sentence-transformers, transformers, etc.) and ease of integration with document parsing libraries. Node.js/Electron for desktop application to provide cross-platform compatibility while maintaining Windows-first approach as specified in constitution.

**Alternatives considered**:
- .NET MAUI (as mentioned in constitution) - rejected due to limited ecosystem for NLP tasks compared to Python
- Rust - rejected due to longer development time despite performance benefits
- Go - rejected due to less mature NLP ecosystem

### Decision: Vector Database Storage
**Rationale**: Selected SQLite with local vector storage instead of dedicated vector database to maintain single-file storage and simplify deployment. This aligns with the "micro-first" principle and keeps the solution lightweight.

**Alternatives considered**:
- ChromaDB - rejected due to additional dependency and complexity
- FAISS - rejected due to memory requirements potentially exceeding 150MB constraint
- Pinecone/Weaviate - rejected due to external service dependency violating privacy requirements

### Decision: Chat Platform Integration
**Rationale**: Using Slack Events API for real-time message processing and Microsoft Graph API for Teams integration. Both approaches allow for webhook-based integration as specified in requirements.

**Alternatives considered**:
- Slack RTM API - rejected due to complexity and real-time connection maintenance
- Teams Bot Framework - rejected due to complexity vs. webhook simplicity

### Decision: Document Parsing
**Rationale**: Using PyMuPDF for PDF parsing and python-docx for Word documents to handle the most common enterprise document formats. HTML parsing via BeautifulSoup for web-based content.

**Alternatives considered**:
- Tika - rejected due to Java dependency
- pdfplumber - considered but PyMuPDF has better performance
- Unstructured.io - rejected due to potential external dependencies

### Decision: Embedding Model
**Rationale**: Using sentence-transformers with CPU-only models to ensure compatibility with standard hardware while maintaining reasonable performance. Selected all-MiniLM-L6-v2 for balance of speed and accuracy.

**Alternatives considered**:
- ONNX models - considered but sentence-transformers provides easier integration
- Ollama - rejected due to additional dependency requirement
- Custom transformer models - rejected due to complexity and resource requirements

### Decision: Encryption Method
**Rationale**: AES-256 for local database encryption as specified in requirements, using Python's cryptography library for FIPS-compliant implementation.

**Alternatives considered**:
- ChaCha20 - rejected due to less standard implementation
- RSA - rejected due to symmetric encryption being more appropriate for local storage

### Decision: Windows Service Implementation
**Rationale**: Using Python's built-in service capabilities with pywin32 for Windows service implementation, allowing the chat monitoring to run in background.

**Alternatives considered**:
- NSSM (Non-Sucking Service Manager) - rejected due to additional dependency
- Windows Task Scheduler - rejected due to less control over service lifecycle