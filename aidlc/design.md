# Gate 3 — Design

Your agent drafts this from `requirements.md`. You check it and sign it.

## Functions in core/

| Function | Takes | Returns |
|---|---|---|
| `ask_zai(system, message)` | the system prompt and the customer's message, both text | the LLM's reply as text |
| `triage(message, ask=ask_zai)` | the customer's message, and the function that asks the LLM (a fake one in tests) | a dict with `category`, `urgency`, `summary` and `draft_reply` |
| `next_action(result)` | the dict from `triage` | `"needs_you"`, `"ignore"` or `"reply"` |

## Errors

| Error | Raised when |
|---|---|
| `ModelBusy` | the LLM still answers 429 after the last retry, answers any other HTTP error, or cannot be reached |
| `UnreadableAnswer` | the answer is not JSON, misses a field, or uses a category or urgency that is not allowed |

## The page

| Page file | What the user does | What they see |
|---|---|---|
| `pages/1_Triage.py` | pastes one message, presses Triage, may edit the draft reply | the "Needs you personally" banner or "Probably safe to ignore", the category, urgency and summary, and the draft reply; a friendly warning or error instead of a crash |

**Approved by:** Reference solution
**Date:** 2026-09-14
