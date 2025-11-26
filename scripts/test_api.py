import httpx
import uuid
from pathlib import Path

API_URL = "http://localhost:8000/analyze"
PDF_FOLDER = Path(__file__).parent.parent / "pdf"

def test_analyze(query: str = None):
    files = []
    for f in PDF_FOLDER.iterdir():
        if f.suffix.lower() in [".pdf", ".jpg", ".jpeg", ".png"]:
            files.append(("files", (f.name, f.read_bytes(), "application/octet-stream")))

    if not files:
        print(f"No files found in {PDF_FOLDER}")
        return

    data = {
        "request_id": str(uuid.uuid4()),
        "user_id": "test_user"
    }
    if query:
        data["query"] = query
    print(f"Sending {len(files)} file(s)...\n")
    response = httpx.post(API_URL, files=files, data=data, timeout=300.0)
    response.raise_for_status()
    result = response.json()
    if "result" in result:
        print(f"Query: {result.get('query', 'N/A')}\n")
        print(result["result"])
    elif "summaries" in result:
        for s in result["summaries"]:
            print(f"File: {s['filename']}\n")
            print(s["summary"])

if __name__ == "__main__":
    import sys
    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else None
    test_analyze(query)
