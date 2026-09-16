# How we work on this project

You are helping a student who has done one Python course. The project is built
in four gates. Each gate produces files, and the student signs each file before
the next gate may begin.

| Gate | Files |
|---|---|
| 1 Intent | `aidlc/intent.md`, written by the student |
| 2 Requirements | `aidlc/requirements.md` |
| 3 Plan | `aidlc/design.md` and `aidlc/tasks.md` |
| 4 Build | one file per task in `aidlc/tasks.md`: `tests/`, then `core/`, then `pages/` |

## Signing

- A gate file is **signed** when its `**Approved by:**` line has a name after it.
- Before you write `aidlc/requirements.md`, `aidlc/intent.md` must be signed.
- Before you write `aidlc/design.md` or `aidlc/tasks.md`, `aidlc/requirements.md`
  must be signed.
- Before you write anything in `tests/`, `core/` or `pages/`, both
  `aidlc/design.md` and `aidlc/tasks.md` must be signed.
- If a file that must be signed is not: write nothing at all, and reply with
  exactly `Not signed yet: sign <file> first.`, naming the file.
- Never fill in an `**Approved by:**` or `**Date:**` line. They belong to the
  student.

## Doing the work

- Do only what the message asks. When it is done, stop. Never start the next
  gate or the next task on your own.
- When you stop, say in one or two sentences what the student should check.
- Write whole files with your file-writing tool. Never paste a file into chat.
- Keep every word of explanation a template already carries; fill in its
  tables and blanks.
- Python 3.14 and Streamlit only. Use nothing that is not in `requirements.txt`.
- Never put a key in code. Code reads `ZAI_API_KEY` from `.env`.
- The first time you use a term a student with one Python course may not know,
  explain it in one plain clause.
- Say plainly what you did not run or did not test.

## Commands

This is Windows PowerShell. Run Python through the project's own interpreter,
and never chain commands with `&&`:

```
.venv\Scripts\python.exe -m pytest
.venv\Scripts\python.exe -m streamlit run app.py
```
