# DriveMind-AI

An AI-powered conversational Google Drive file discovery assistant built using FastAPI, LangChain, Streamlit, and Google Drive API.

---

## Live Deployment

### Frontend (Streamlit)
https://drivemind-ai-8zxelyfjyh74p47pduwvzk.streamlit.app/

### Backend API Docs (FastAPI Swagger)
https://drivemind-ai.onrender.com/docs

---

## Features

- Conversational AI file discovery
- Google Drive API integration
- LangChain AI agent with tool calling
- Natural language file search
- Search by:
  - file name
  - file type
  - file content
  - modified date
- PDF, image, and Excel file retrieval
- Clickable Google Drive links
- Streamlit chat interface
- FastAPI REST API backend

---

## Tech Stack

- FastAPI
- LangChain
- Groq LLM
- Streamlit
- Google Drive API
- Python

---

## Architecture

User  
↓  
Streamlit Frontend  
↓  
FastAPI Backend  
↓  
LangChain Agent  
↓  
Drive Search Tool  
↓  
Google Drive API

---

## Example Queries

- Find PDF reports
- Search for invoice image
- Find employee excel sheet
- Open daily report pdf
- Find image files
- Search salary spreadsheet

---

## API Endpoints

### GET /

Health check endpoint.

### POST /chat

Chat endpoint for conversational file discovery.

Example request:

```json
{
  "message": "Find PDF reports"
}
