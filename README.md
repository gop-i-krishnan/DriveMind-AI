# DriveMind-AI

An AI-powered conversational Google Drive file discovery assistant built using FastAPI, LangChain, Streamlit, and Google Drive API.

---

## Live Deployment

| | |
|---|---|
| **Frontend (Streamlit)** | https://drivemind-ai-8zxelyfjyh74p47pduwvzk.streamlit.app/ |
| **Backend API Docs (FastAPI Swagger)** | https://drivemind-ai.onrender.com/docs |

---

## Features

- Conversational AI file discovery
- Google Drive API integration
- LangChain AI agent with tool calling
- Natural language file search
- Search by file name, file type, file content, or modified date
- PDF, image, and Excel file retrieval
- Clickable Google Drive links
- Streamlit chat interface
- FastAPI REST API backend

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI |
| AI Agent | LangChain |
| LLM | Groq |
| Storage | Google Drive API |
| Language | Python |

---

## Architecture

```
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
```

---

## API Endpoints

### `GET /`

Health check endpoint. Returns service status.

### `POST /chat`

Chat endpoint for conversational file discovery.

**Request body:**

```json
{
  "message": "Find PDF reports"
}
```

**Response:**

```json
{
  "reply": "Here are the PDF reports I found in your Drive: ..."
}
```

> Full interactive API docs available at: https://drivemind-ai.onrender.com/docs

---

## Example Queries

- Find PDF reports
- Search for invoice image
- Find employee excel sheet
- Open daily report PDF
- Find image files
- Search salary spreadsheet

---

## Local Setup

### 1. Clone Repository

```bash
git clone https://github.com/gop-i-krishnan/DriveMind-AI.git
cd DriveMind-AI
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Add Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> **Note:** The deployed version uses cloud-hosted secrets (Render environment variables / Streamlit secrets). For local development, the `.env` file is used. Never commit your `.env` file to version control.

### 6. Add Google Credentials

Place your service account JSON file at:

```
credentials/service_account.json
```

### 7. Run Backend

```bash
uvicorn backend.main:app --reload
```

### 8. Run Frontend

```bash
streamlit run frontend/app.py
```

---

## Future Improvements

- Conversational memory across sessions
- Advanced natural language query parsing
- In-app file previews
- User authentication and multi-user support
- Multi-folder and shared drive support
- Vector search integration
- RAG-based document understanding

---

## Author

**Gopi Krishnan**  
[GitHub](https://github.com/gop-i-krishnan)
