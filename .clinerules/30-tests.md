---
paths:
  - "tests/**"
---
# Writing tests

- Write one test for each `pytest` row in `aidlc/requirements.md`, named exactly
  as the row names it.
- Never call the real model or the network. Hand the function under test a fake
  model: a small function that returns a fixed reply.
- Import from `core/` **inside each test function**, not at the top of the file.
  Before the code exists, every test then fails on its own, and pytest shows how
  many.
- Test what the code decides, not what the model would say.
- Cover: a well-formed answer, an answer that is not JSON, an answer missing a
  field or using a value that is not allowed, and the model being busy.
- After writing the file, run `.venv\Scripts\python.exe -m pytest` and report the
  last line. Every test must fail. If any passes, say so: it cannot be testing
  code that does not exist yet.
