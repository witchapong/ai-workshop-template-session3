# Gate 3 — Tasks

Your agent drafts this with `design.md`. You check it and sign it.

Three tasks, one file each, always in this order: the tests, then the code,
then the page. Writing the tests first proves they can fail before any code
exists.

| # | Task | The one file it touches | Done when |
|---|---|---|---|
| 1 | Write the tests, using a fake LLM | `tests/test_triage.py` | `pytest` runs and all 8 tests fail |
| 2 | Write the LLM call and the two decisions | `core/triage.py` | requirements 1–8: all 8 tests pass |
| 3 | Write the page | `pages/1_Triage.py` | requirements 9–12 |

**Approved by:** Reference solution
**Date:** 2026-09-14
