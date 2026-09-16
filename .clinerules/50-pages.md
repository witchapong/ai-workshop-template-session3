---
paths:
  - "pages/**"
  - "app.py"
---
# Writing a page

- The page calls functions in `core/`. It decides nothing itself.
- Disable the button while the text box is empty.
- Show `st.spinner` while waiting, saying it can take up to two minutes when the
  room is busy.
- Catch the "busy" error and show `st.warning` asking to press the button again.
  Catch the "couldn't read the answer" error and show `st.error`. Never let a
  traceback reach the page.
- Keep the latest result in `st.session_state`. Editing any box reruns the page,
  and a result that only exists inside `if st.button(...)` disappears.
- After writing the file, give the command that starts the app and list the EYES
  rows to check.
