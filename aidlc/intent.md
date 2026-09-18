# Gate 1 — Intent

This is the one file you write yourself, and the only one where detail
matters. Every later gate is built from it: something you leave out here is
something nobody builds, and nobody checks. Write your answer under each
question.

**Who is this for?**
Fah, who runs a small clothing shop on Instagram and LINE from her dorm.

**What problem does it solve?**
She gets forty to sixty messages a night and answers them in the order they
arrived, not the order that matters. Urgent complaints get buried.

**What does "done" look like?**
- I paste one message and press Triage, and see its category (order,
  complaint, question or other), how urgent it is, a one-line summary, and a
  draft reply in the customer's language
- A high-urgency complaint shows a red "Needs you personally" banner
- Anything that is not a real customer message shows "Probably safe to
  ignore" and no draft reply
- If the LLM is busy, the page tells me and lets me try again — never a
  blank page or an error screen
- If the LLM's answer can't be read, the page says so — never half a result

**What is deliberately NOT included?**
Saving messages, sending replies, logins, connecting to LINE or Instagram, and
more than one message at a time.

## Size check

Tick every box before you sign. If one will not tick, cut the idea down.

- [x] One page
- [x] At most three bullets under "What does done look like?", plus the two about a busy LLM and an unreadable answer
- [x] One LLM call per button press
- [x] No logins, no saved history
- [x] No outside service except the LLM
- [x] I can say in one sentence what my code decides from the LLM's answer:
  a high-urgency complaint gets the "Needs you personally" banner, and
  anything classed "other" is marked safe to ignore.

**Approved by:** Reference solution
**Date:** 2026-09-14
