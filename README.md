# AI for Software Development — Session 3

Two apps today, both built by your agent through four gates — checkpoints
where you read and sign what the agent wrote before it goes on. This page is
setup only; the labs are in `labs/LAB3.md` and `labs/LAB4.md`.

The lab PCs are wiped between sessions, so every step below is needed every
time, even if you did it last week.

## Setup for Lab 3 — nine steps, about ten minutes

1. **Make your own copy.** Click **Use this template** → **Create a new
   repository**. Name it `lab3-triage`, set it to **Public**, and leave
   **Include all branches** off.
2. **Clone it and open it.** In VS Code's terminal:
   ```
   git clone <the URL of your new repository>
   ```
   Then **File → Open Folder** on `lab3-triage`, and click **Trust Folder &
   Continue**.

   Does it say `git` **is not recognized**? Git is missing from this PC. Install
   it, then close the terminal and open a new one before trying the clone again:
   ```
   winget install --id Git.Git -e
   ```
   If that fails too, download the installer from `https://git-scm.com/download/win`
   and accept every default. Git is needed all morning, not just here: it is how
   you catch up if you fall behind, and how you push your work before you leave.
3. **Create the venv**, a private copy of Python for this project:
   ```
   py -3.14 -m venv .venv
   ```
4. **Install the packages:**
   ```
   .venv\Scripts\python.exe -m pip install -r requirements.txt
   ```
5. **Copy in your key:**
   ```
   copy .env.example .env
   ```
   Open `.env`, replace `paste-your-key-here` with the key from the projector,
   save, and close the tab. A key on screen is a key shared.
6. **Check everything works:**
   ```
   .venv\Scripts\python.exe check_setup.py
   ```
   Carry on only when it prints `ALL CHECKS PASSED`.
7. **Install Cline.** When VS Code offers to install the recommended
   extensions, click **Install**. No offer? Open **Extensions** (the four
   squares on the left), search `saoudrizwan.claude-dev`, and install it.
   Either way, check the dialog names `cline.bot`, then click **Trust
   Publisher & Install**.
8. **Point Cline at the LLM.** Click the robot icon on the left.
   1. Choose **Bring my own API key**. It is the fourth option; scroll if you
      cannot see it.
   2. The provider box starts on **OpenRouter**. Click it, type `compatible`,
      and pick **OpenAI Compatible**.
   3. Base URL: `https://api.z.ai/api/coding/paas/v4`
   4. API key: the key from the projector.
   5. Model ID: type `glm-5.3-flash`.
9. **Say hello.** Type `hello` to Cline and wait for a reply.

Cline says `429`? The whole room is asking at once. Wait ten seconds and send
it again.

## Setup for Lab 4 — five steps, about five minutes

1. **Make a second copy** of this template. Name it `lab4-` plus your idea,
   for example `lab4-repair-requests`.
2. **Clone it into the same folder that holds `lab3-triage`**, and open it.
   Your terminal is still inside `lab3-triage`, so go up one folder first:
   ```
   cd ..
   git clone <the URL of your new repository>
   ```
   Then **File → Open Folder** on the new folder, and click **Trust Folder &
   Continue**.
3. **Create the venv:**
   ```
   py -3.14 -m venv .venv
   ```
4. **Install the packages:**
   ```
   .venv\Scripts\python.exe -m pip install -r requirements.txt
   ```
5. **Copy your key across from Lab 3, and check:**
   ```
   copy ..\lab3-triage\.env .env
   .venv\Scripts\python.exe check_setup.py
   ```
   If `copy` says it cannot find the file, run `copy .env.example .env`
   instead, open `.env`, replace `paste-your-key-here` with the key from the
   projector, and run the check again.

Cline is already set up on this PC. There is nothing to redo.

## What is in here

| Path | What it is for |
|---|---|
| `aidlc/` | The four gate documents: intent, requirements, design, tasks |
| `.clinerules/` | The rules your agent follows. You do not need to edit them |
| `lab3/scenario.md` | Lab 3's shop, and six messages to test your app with |
| `labs/` | The two lab manuals |

## Leaving

Push before you stand up. Nothing left on a lab PC is there next time.

```
git add -A
git commit -m "done for today"
git push
```

`.env` is never pushed: it holds a password, and `.gitignore` keeps it off
GitHub.

Something broken? See `TROUBLESHOOTING.md`.
