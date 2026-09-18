"""Customer inbox triage: paste one message, see what to do about it."""

import streamlit as st

from core.triage import ModelBusy, UnreadableAnswer, next_action, triage

st.title("Customer inbox triage")
st.caption("Paste one customer message. The model reads it; the code decides what happens next.")

message = st.text_area("Customer message", height=150)

if st.button("Triage", type="primary", disabled=not message.strip()):
    st.session_state.pop("result", None)
    try:
        with st.spinner("Asking the model. This can take up to two minutes when the room is busy."):
            st.session_state["result"] = triage(message)
    except ModelBusy as error:
        st.warning(f"{error} Press Triage again in a moment.")
    except UnreadableAnswer as error:
        st.error(f"Couldn't read the model's answer. {error} Press Triage to try again.")

# Kept in session_state: editing the draft reply reruns the page, and a result
# that only existed inside the button's `if` would vanish mid-edit.
result = st.session_state.get("result")
if result:
    action = next_action(result)
    if action == "needs_you":
        st.error("Needs you personally")
    if action == "ignore":
        st.info("Probably safe to ignore")
    st.write(f"**Category:** {result['category']}  ·  **Urgency:** {result['urgency']}")
    st.write(f"**Summary:** {result['summary']}")
    if action != "ignore":
        st.text_area("Draft reply (edit before sending)", result["draft_reply"], height=120)
