# If something breaks

Work down this list. Each fix takes under two minutes. Still stuck after ten
minutes? Ask a neighbour before the instructor: they have probably hit the same
thing.

## Setup

**`git` "is not recognized"**
Git is not installed on this PC. Install it, then close the terminal and open a
new one: `winget install --id Git.Git -e`. If `winget` is missing too, download
the installer from `https://git-scm.com/download/win` and accept every default.
You need Git for more than the first clone: "Catching up" in `labs/LAB3.md` uses
it, and so does pushing your work before you leave.

**`python` or `pytest` "is not recognized"**
The venv is never activated, on purpose, so bare `python` and `pytest` do not
exist here. Always name the project's interpreter:
`.venv\Scripts\python.exe check_setup.py`,
`.venv\Scripts\python.exe -m pytest`. Before a `.venv` exists, use `py -3.14`.

**`Activate.ps1 cannot be loaded because running scripts is disabled`**
Do not activate the venv. Skip that and use `.venv\Scripts\python.exe` as above.

**`The token '&&' is not a valid statement separator`**
This PowerShell cannot chain commands with `&&`. Type each command on its own
line.

**`check_setup.py` says a package is missing**
Run `.venv\Scripts\python.exe -m pip install -r requirements.txt`, then the
check again.

**`check_setup.py` says the key was rejected**
Open `.env`. The line must read `ZAI_API_KEY=` followed by the whole key, with
no spaces, no quotes, and nothing left of `paste-your-key-here`.

**`check_setup.py` says the key is busy**
The room is busy. Wait ten seconds and run it again.

**There is no `.env` file**
Run `copy .env.example .env`, then paste your key in.

## Cline

**There is no robot icon on the left**
Cline is not installed, or you installed a copy with a similar name. Open
**Extensions**, search `saoudrizwan.claude-dev`, and install the one published
by `cline.bot`.

**Cline wants me to sign in or pay**
You chose one of the first three options. Open Cline's settings (the gear at
the top of its panel) and choose **Bring my own API key**.

**Every Cline request fails with a message about billing or balance**
The Base URL is wrong. It must be exactly
`https://api.z.ai/api/coding/paas/v4`, with `coding` in it.

**I cannot find `glm-5.3-flash` in a list**
There is no list. With **OpenAI Compatible** chosen, type the model ID into
its box.

**Cline says `429`**
The room is busy. Wait ten seconds and send it again. Change nothing.

**I typed to Cline and my message vanished**
Cline is waiting for you to click something: **Save**, **Proceed**, or **Resume
Task**. Click it, or cancel, then type again.

**Cline asks me to click Save more than once for one file**
Normal. Keep clicking **Save** until it moves on.

**Cline shows a command as Skipped and says Thinking… for minutes**
It is waiting for you but shows no button. Click **Cancel**, then **Resume
Task**.

**Start New Task does nothing**
The old task still has something pending. Approve or cancel it. If that does
not free it: **Ctrl+Shift+P** → **Developer: Reload Window**, then check the
model name at the bottom of the Cline box.

## Gates

**Cline replied `Not signed yet: sign <file> first.`**
It is right. Open that file, check it, type your name after
`**Approved by:**` and today's date after `**Date:**`, save, and send the
prompt again in a new task.

**Cline started the next gate by itself**
Click **Cancel**. Open a new task and type the next prompt yourself. Each gate
has its own prompt for a reason.

**The class moved on and my agent is still working**
Let it finish only if it is nearly done. Otherwise cancel the task and use
"Catching up" in `labs/LAB3.md`.

**After task 1, `pytest` says `1 error` instead of a number failed**
The tests import from `core/` at the top of the file. Tell Cline: "Move each
import from core inside the test that uses it."

**After task 1, some tests already pass**
They cannot be testing code that does not exist yet. Tell Cline which ones, and
ask it to make them test the code.

**`pytest` says "no tests ran"**
There are no tests yet. That is expected until task 1.

## The app

**I pressed Triage and nothing happened**
The first press only saves what you typed and turns the button red. Press
**Triage** again.

**The page says the model is busy**
The room is busy. Press the button again in a moment.

**The page says it could not read the model's answer**
The model answered in the wrong shape. Press the button again; it usually works
the second time.

**The page is blank, or shows a red error trace**
Copy the last line of the trace into Cline and ask it to fix the page so the
error becomes a friendly message.

**My change does not show in the app**
Save the file, then press **R** in the browser tab, or click **Rerun** at the
top right of the page.
