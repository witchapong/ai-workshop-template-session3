---
paths:
  - "aidlc/requirements.md"
---
# Writing aidlc/requirements.md

- Read `aidlc/intent.md` first. Keep the template's explanation; fill in its table.
- One numbered row per requirement. Every row's check must be able to fail.
- There are exactly two kinds of check:
  - `pytest test_<name>` when plain code in `core/` decides the result.
  - `EYES: open <page>, do <action>, see <exact thing>` when it is about what a
    page shows. A person checks it by looking at the running app.
- Every bullet under "What does done look like?" in `intent.md` gets at least
  one row.
- At least one EYES row names an exact thing to see, such as a banner's words.
- The model's own judgement is never a `pytest` row. Tests use a fake model, so
  a `pytest` row can only check what the code does with an answer, for example
  what it decides when the answer says `complaint` and `high`.
- An EYES row checks what the page does, never the model's exact category or
  urgency. Those vary from run to run.
- Include a `pytest` row for each of: an answer that is not JSON, an answer
  missing a field or using a value that is not allowed, and the model being busy.
