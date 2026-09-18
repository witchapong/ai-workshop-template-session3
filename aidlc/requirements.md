# Gate 2 — Requirements

Your agent drafts this from `intent.md`. You check it, correct it, and sign it.

Each row is one thing the app must do, with a check that could fail. There are
two kinds of check:

- `pytest test_<name>` — a test runs plain code in `core/` with a fake LLM.
- `EYES: open <page>, do <action>, see <exact thing>` — you look at the running
  app.

A check that could never fail is not a check.

| # | Requirement | Check |
|---|---|---|
| 1 | A well-formed answer gives back its category, urgency, summary and draft reply | `pytest test_reply_fields_come_through` |
| 2 | A complaint marked high urgency needs Fah personally | `pytest test_complaint_high_needs_you` |
| 3 | A complaint that is not high urgency just gets a reply | `pytest test_complaint_not_high_gets_a_reply` |
| 4 | Anything classed "other" is marked safe to ignore | `pytest test_other_is_ignored` |
| 5 | An answer that is not JSON is reported as unreadable, never half-used | `pytest test_invalid_json_is_unreadable` |
| 6 | An answer missing a field is reported as unreadable | `pytest test_missing_field_is_unreadable` |
| 7 | An answer using a category we do not allow is reported as unreadable | `pytest test_unknown_category_is_unreadable` |
| 8 | A busy LLM is reported as busy, not a crash | `pytest test_busy_model_raises_busy` |
| 9 | An urgent complaint is flagged on the page | `EYES: open Triage, paste message 3 from lab3/scenario.md, press Triage, see the red "Needs you personally" banner and a draft reply in Thai` |
| 10 | Spam is marked safe to ignore on the page | `EYES: open Triage, paste message 6, press Triage, see "Probably safe to ignore" and no draft reply box` |
| 11 | An ordinary order gets a draft reply that stays while it is edited | `EYES: open Triage, paste message 1, press Triage, see no banner and a draft reply; type in the draft reply box and see the result stay on screen` |
| 12 | A busy or unreachable LLM gives a friendly message | `EYES: turn off the PC's network, paste any message, press Triage, see a yellow message asking to press Triage again, and no error trace` |

**Approved by:** Reference solution
**Date:** 2026-09-14
