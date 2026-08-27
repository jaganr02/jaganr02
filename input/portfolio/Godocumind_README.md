# GoDocuMind

A Golang-based document analysis platform for processing TXT, PDF, and DOCX files through REST APIs.

The application extracts useful document insights such as word count, character count, reading time, keywords, and summaries using a modular backend architecture.

---

## Features

- Upload TXT, PDF, and DOCX documents
- Document statistics
  - Word Count
  - Character Count
  - Line Count
  - Reading Time
- Keyword Extraction
- Document Summary
- Responsive Web Interface
- REST API Architecture
- Modular Parser Design

---

## Tech Stack

### Backend
- Golang
- net/http
- encoding/json
- io
- os
- filepath
- strings
- sort

### Frontend
- HTML5
- CSS3
- JavaScript

### Libraries
- github.com/ledongthuc/pdf
- github.com/nguyenthenguyen/docx

---

## Project Structure

```
GoDocuMind
│
├── parsers
│   ├── txt.go
│   ├── pdf.go
│   └── docx.go
│
├── static
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── uploads
├── main.go
├── go.mod
├── go.sum
└── README.md
```

---

## Getting Started

### Clone

```bash
git clone https://github.com/your-username/godocumind.git
```

### Install Dependencies

```bash
go mod tidy
```

### Run

```bash
go run .
```

Open:

```
http://localhost:8080
```

---

## Supported File Formats

- TXT
- PDF
- DOCX

---

## Future Enhancements

- Advanced document summarization
- Improved keyword extraction
- Search functionality
- Database integration
- User authentication
- LLM integration
- Vector Database
- RAG Pipeline
- Multi-Agent Architecture

---

## Author

**R Jagan**

B.Tech Artificial Intelligence & Data Science
