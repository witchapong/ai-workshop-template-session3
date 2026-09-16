# Lab 3 — Customer inbox triage

**What you build:** a page where a shop owner pastes one customer message and
sees what kind it is, how urgent it is, what it says in one line, and a draft
reply. The model reads the message. Your code decides what happens next.

**Time:** Gate 1, 10 minutes on your own. Gates 2 to 4, 40 minutes, following
your instructor.

**Before you start:** "Setup for Lab 3" in `README.md`, all nine steps, with
`check_setup.py` printing `ALL CHECKS PASSED`.

**Gates 2 to 4 are a follow-along.** Your instructor types each prompt on the
projector; you type the same prompt into a new Cline task on your PC at the same
moment, and check and sign your own file when the instructor does. If Cline
starts the next gate by itself, click **Cancel**. Falling behind? See "Catching
up" near the end of this file.

**To sign a file:** type your name after `**Approved by:**` and today's date
after `**Date:**`, then save. Cline will not start a gate whose input is
unsigned.

---

## Gate 1 — Intent (10 minutes)

The only file you write yourself.

1. Open `lab3/scenario.md` and read Fah's story.
2. Open `aidlc/intent.md` and write an answer under each of its four questions.
3. Tick all six size-check boxes. For the last one, write the sentence: what
   does your code decide from the model's answer?
4. **Only now**, scroll to "The reference intent" at the end of this file. Add
   anything you missed.
5. Sign `aidlc/intent.md`.

## Gate 2 — Requirements

1. Open a new Cline task and type:

   ```
   Read aidlc/intent.md.
   Write aidlc/requirements.md.
   ```

2. You get `aidlc/requirements.md`, a table of numbered rows.
3. Check it:
   - every bullet under "What does done look like?" in your intent has a row
   - `pytest` rows test what the code decides, never what the model thinks
   - `EYES` rows say what to open, what to do, and exactly what you will see
   - there are rows for an answer that is not JSON, an answer missing a field,
     and a busy model

   Anything wrong or missing? Tell Cline what to change, in the same task.
4. Sign `aidlc/requirements.md`.

## Gate 3 — Design and tasks

1. Open a new Cline task and type:

   ```
   Read aidlc/requirements.md.
   Write aidlc/design.md and aidlc/tasks.md.
   ```

2. You get `aidlc/design.md` and `aidlc/tasks.md`.
3. Check them:
   - `design.md` has a separate function that calls the model, **passed in** to
     the function that uses it, so a test can hand in a fake
   - `tasks.md` has exactly three tasks, one file each, in this order:
     `tests/test_triage.py`, `core/triage.py`, `pages/1_Triage.py`
4. Sign both files.

## Gate 4 — Build, one task at a time

### Task 1 — the tests

1. Open a new Cline task and type:

   ```
   Read aidlc/tasks.md.
   Do task 1.
   ```

2. You get `tests/test_triage.py`.
3. Run the tests:

   ```
   .venv\Scripts\python.exe -m pytest
   ```

   The last line must say a number **failed**, such as `8 failed`. That is
   right: the code does not exist yet. See `1 error`, or anything passing? See
   "Gates" in `TROUBLESHOOTING.md`.

### Task 2 — the code

1. Open a new Cline task and type:

   ```
   Read aidlc/tasks.md.
   Do task 2.
   ```

2. You get `core/triage.py`.
3. Run the tests again. Every test must now **pass**.

### Task 3 — the page

1. Open a new Cline task and type:

   ```
   Read aidlc/tasks.md.
   Do task 3.
   ```

2. You get `pages/1_Triage.py`.
3. Start the app:

   ```
   .venv\Scripts\python.exe -m streamlit run app.py
   ```

4. Open **Triage** in the sidebar. Put all six messages from
   `lab3/scenario.md` through it; each must do what its row says. After
   pasting a message you may need to press **Triage** twice, because the first
   press saves the text.
5. Work through every `EYES` row in `aidlc/requirements.md`.

## You are done when

- [ ] `aidlc/` holds four signed files
- [ ] `pytest` shows every test passing
- [ ] message 3 shows **Needs you personally**, message 6 shows **Probably safe to ignore**, and the other four show a draft reply and no banner
- [ ] you can point to the line in `core/triage.py` that decides the banner

Then push (see "Leaving" in `README.md`).

## Catching up

Your instructor moves on after about eight minutes at each prompt. If your agent
is still working then, let it finish only if it is nearly done. Otherwise cancel
the Cline task and take that step's finished file from the template, so you
stay in step.

Each time you catch up, type this first, even if you typed it before:

```
git fetch https://github.com/witchapong/ai-workshop-template-session3 solution/lab3
```

Then type the line for the step you are on. `FETCH_HEAD` in it is git's name
for what the `git fetch` line just downloaded; another fetch would replace
that, which is why the fetch line comes first every time.

| Still at | Type |
|---|---|
| Gate 2 | `git checkout FETCH_HEAD -- aidlc/requirements.md` |
| Gate 3 | `git checkout FETCH_HEAD -- aidlc/design.md aidlc/tasks.md` |
| Task 1 | `git checkout FETCH_HEAD -- tests` |
| Task 2 | `git checkout FETCH_HEAD -- core` |
| Task 3 | `git checkout FETCH_HEAD -- pages` |

**Once you take one finished file, take every later one the same way.** The
finished files fit each other; your own agent's files may use different names.
If your own agent made a file with a different name in that folder, delete it,
or pytest will run both.

About to start Lab 4 without a working Lab 3? Take everything at once:

```
git checkout FETCH_HEAD -- aidlc tests core pages
```

---

## The reference intent

**Do not read this until you have written yours.** Compare, and add what you
missed.

```markdown
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
- Anything that is not a real customer message shows "Probably safe to ignore" and no draft reply
- If the model is busy, the page tells me and lets me try again — never a
  blank page or an error screen
- If the model's answer can't be read, the page says so — never half a result

**What is deliberately NOT included?**
Saving messages, sending replies, logins, connecting to LINE or Instagram, and
more than one message at a time.

**What my code decides from the model's answer:**
A high-urgency complaint gets the "Needs you personally" banner, and anything
classed "other" is marked safe to ignore.
```
