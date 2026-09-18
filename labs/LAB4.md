# Lab 4 — Your own project

**What you build:** anything you like, built exactly the way you built Lab 3.
The same prompts, the same rules, the same templates. The only new thing
is your `intent.md`.

**Time:** setup 5 minutes, Gate 1 10 minutes, Gates 2 to 4 until 11:40, then
ten minutes to get your demo ready.
**Stop building at 11:40.** Whatever works then is your demo.

**Before you start:** "Setup for Lab 4" in `README.md`, all five steps.

**Every prompt goes into a new Cline task.** If Cline starts the next gate by
itself, click **Cancel** and type the next prompt yourself.

---

## Gate 1 — Your intent (10 minutes)

1. Pick an idea. Stuck for one? Take one from "Ideas" below, or change one.
2. Open `aidlc/intent.md` and write an answer under each of its four questions.
3. Do the size check. Every box must tick. If one will not, cut the idea down
   (see "Cutting an idea down").
4. Write the last box's sentence: what does your code decide from the LLM's
   answer? A page that only shows the LLM's answer is not enough.
5. Sign `aidlc/intent.md`.

### Cutting an idea down

| Too big | Cut down to |
|---|---|
| A second-hand marketplace for the dorm | Paste one listing. The LLM pulls out the item, its condition and the price; the code says **fair price**, **overpriced** or **check the photos** |
| A study-group finder | Paste one "anyone studying…" post. The LLM pulls out subject, time and place; the code says **starts within an hour** or **later today** |

### Ideas

| Text that comes in | What the LLM pulls out | What your code decides |
|---|---|---|
| A dorm repair request | type, urgency, room | an urgent electrical fault → "call the dorm office now" |
| A club event sign-up | event, headcount, dietary needs | over capacity → waitlist |
| A batch of lecture feedback | topics, mood, questions asked | three or more confused on one topic → revisit it next class |
| A product review | problem, sentiment, draft reply | one star plus a safety word → escalate |
| An internship posting | skills wanted, deadline | deadline within three days → apply today |
| Meeting notes | action items, owners, dates | an item with no owner → flag it |

---

## Gate 2 — Requirements

1. Open a new Cline task and type:

   ```
   Read aidlc/intent.md.
   Write aidlc/requirements.md.
   ```

2. You get `aidlc/requirements.md`.
3. Check it: every "done" bullet has a row; `pytest` rows test what your code
   decides; `EYES` rows say exactly what you will see; there are rows for an
   answer that is not JSON, a missing field, and a busy LLM.
4. Sign it.

## Gate 3 — Design and tasks

1. Open a new Cline task and type:

   ```
   Read aidlc/requirements.md.
   Write aidlc/design.md and aidlc/tasks.md.
   ```

2. You get `aidlc/design.md` and `aidlc/tasks.md`.
3. Check them: the LLM call is a separate function, passed in; three tasks,
   one file each, in the order tests, code, page.
4. Sign both files.

## Gate 4 — Build

### Task 1 — the tests

1. Open a new Cline task and type:

   ```
   Read aidlc/tasks.md.
   Do task 1.
   ```

2. Run `.venv\Scripts\python.exe -m pytest`. Every test must **fail**.

### Task 2 — the code

1. Open a new Cline task and type:

   ```
   Read aidlc/tasks.md.
   Do task 2.
   ```

2. Run the tests again. Every test must **pass**.

### Task 3 — the page

1. Open a new Cline task and type:

   ```
   Read aidlc/tasks.md.
   Do task 3.
   ```

2. Start the app with `.venv\Scripts\python.exe -m streamlit run app.py`. Try
   it on your own real examples, and work through every `EYES` row.

## Stuck

In this order:

1. **Re-read `intent.md`.** Most stalls come from an intent that is too big or
   too vague. Cut one "done" bullet, sign it again, and carry on.
2. **`TROUBLESHOOTING.md`**, for setup and Cline problems.
3. **At 11:40, stop building.** Whatever works is your demo.

## Random demos (11:50)

Nothing is graded and nothing is handed in.

The instructor picks four or five students at random to demo, each for about
two minutes, right up to the 12:00 close. Anyone may be picked, so have your
app running.

| Clock | What |
|---|---|
| 11:50 | First demo |
| 12:00 | Close |

If you are picked, give three things in about two minutes:

1. Your intent, in one sentence.
2. Your app, on one real input.
3. The one thing your code decides.

When you are not demoing, watch for one idea you could steal for your own
project.

Push your work afterwards if you want it for your portfolio.
