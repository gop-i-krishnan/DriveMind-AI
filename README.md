# DriveMind-AI Drive Assistant

An AI-powered conversational file discovery assistant built using FastAPI, LangChain, Streamlit, and Google Drive API.

## Features

- Conversational AI file search
- Google Drive integration
- AI agent with tool calling
- Natural language search
- PDF, image, and Excel file discovery
- Clickable Google Drive links
- Streamlit chat interface

## Tech Stack

- FastAPI
- LangChain
- Groq LLM
- Streamlit
- Google Drive API
- Python

## Architecture

User → Streamlit Frontend → FastAPI Backend → LangChain Agent → Drive Search Tool → Google Drive API

## Example Queries

- Find PDF reports
- Search for invoice image
- Find employee excel file
- Open daily report pdf

## Setup Instructions

### Clone Repository

```bash
git clone <your-github-link>
cd TailorTalk_assignment
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Add Environment Variables

Create `.env`

```env
GROQ_API_KEY=your_api_key
```

### Add Google Credentials

Place service account JSON inside:

```text
credentials/service_account.json
```

### Run Backend

```bash
uvicorn backend.main:app --reload
```

### Run Frontend

```bash
streamlit run frontend/app.py
```

## Future Improvements

- Conversational memory
- Advanced query parsing
- File previews
- Authentication
- Multi-folder support