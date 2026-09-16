---
paths:
  - "core/**"
---
# Calling the model from core/

- **The model turns messy language into fields. Every decision about those
  fields is plain Python.** No arithmetic, storage or decisions happen inside
  the model.
- Address `https://api.z.ai/api/coding/paas/v4/chat/completions`, model
  `glm-5.3-flash`.
- Read the key with `load_dotenv(Path(__file__).resolve().parent.parent / ".env")`,
  then `os.environ.get("ZAI_API_KEY", "")`.
- Use Python's built-in `urllib.request`. Add no package.
- Send the system prompt and the user's text as two messages, with
  `"response_format": {"type": "json_object"}`, `"thinking": {"type": "disabled"}`
  and `"max_tokens": 800`. Time out after 30 seconds.
- On HTTP 429 (too many requests), wait 2 seconds, then 4, then 8, each plus
  `random.random()` seconds, and try again. After the last retry, raise the
  "busy" error. Raise the same error, with a message saying which, for any other
  HTTP error or a network failure.
- Parse the answer as JSON. If it is not JSON, is missing a field, or uses a
  value outside its allowed list, raise the "couldn't read the answer" error.
  Never return half a result.
- The system prompt names every field and every allowed value, and asks for
  JSON only.
- After writing the file, run `.venv\Scripts\python.exe -m pytest` and report the
  last line.
