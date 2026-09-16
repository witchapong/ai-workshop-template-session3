---
paths:
  - "aidlc/design.md"
  - "aidlc/tasks.md"
---
# Writing aidlc/design.md and aidlc/tasks.md

Read `aidlc/requirements.md` first.

## design.md

- A function table: name, what it takes, what it returns. Every `pytest` row in
  `requirements.md` is covered by a function in it.
- The function that calls the model is separate, and is **passed in** as an
  argument to the function that uses it, with the real function as its
  default, so a test can hand in a fake.
- Two error types: one for "the model is busy or unreachable", one for "the
  model's answer could not be read".
- A page table: the one page, what the user does there, what they see.

## tasks.md

- Exactly three tasks, one file each, and no file owned by two tasks:
  1. `tests/test_<app>.py`
  2. `core/<app>.py`
  3. `pages/1_<App>.py`
- `<app>` is the project's short name in lower case.
- Each task's "Done when" comes from `requirements.md`:
  1. `pytest` runs and every test fails, because nothing exists yet
  2. every `pytest` row passes
  3. every EYES row
