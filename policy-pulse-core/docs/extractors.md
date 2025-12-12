# Extractors Module Documentation

## Overview
The extractors module is responsible for extracting content from various document formats and preparing them for policy analysis. This module handles parsing of documents from SharePoint, Confluence, Google Drive, and other sources.

## Supported Formats
- PDF documents
- Microsoft Word documents (.docx)
- Plain text files
- HTML content
- Confluence pages
- SharePoint documents

## Architecture
The extractors module follows a plugin-based architecture where each document format has its own extractor class:

```
extractors/
├── base.py          # Base extractor interface
├── pdf_extractor.py # PDF document extractor
├── docx_extractor.py # Microsoft Word extractor
├── txt_extractor.py # Plain text extractor
├── html_extractor.py # HTML content extractor
└── api_extractors/  # API-based extractors
    ├── confluence_extractor.py
    └── sharepoint_extractor.py
```

## Usage
The extractors are typically used by the RAG (Retrieval-Augmented Generation) system to process documents before they are stored in the vector database.

## Configuration
Extractor behavior can be configured through the main configuration file, including:
- Document processing timeouts
- Maximum file sizes
- Supported file types
- Authentication settings for API extractors