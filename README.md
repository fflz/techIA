# Resume Analysis API

Extract text from resumes (PDF/images) via OCR and answer recruitment queries using LLM.

## Setup

1. Create virtual environment and install dependencies:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and configure:
```bash
cp .env.example .env
```

3. Start MongoDB (WSL/Docker):
```bash
docker run -d --name mongodb -p 27017:27017 mongo:7
```

## Configuration

| Variable | Description |
|----------|-------------|
| `LLM_PROVIDER` | `openrouter` or `gemini` |
| `OPENROUTER_API_KEY` | OpenRouter API key |
| `OPENROUTER_MODEL` | Model name (e.g., `anthropic/claude-3-haiku`) |
| `GEMINI_API_KEY` | Google Gemini API key |
| `GEMINI_MODEL` | Model name (e.g., `gemini-2.5-flash`) |
| `MONGODB_URI` | MongoDB connection string |

## Run

```bash
python main.py
```

API available at http://localhost:8000

Swagger docs at http://localhost:8000/docs

## API Usage

**POST /analyze**

Form data:
- `files`: PDF or image files (JPG/PNG)
- `request_id`: Unique request ID
- `user_id`: User identifier
- `query`: (optional) Recruitment query

Without query: returns summaries of each resume

With query: returns ranked matches with justifications
