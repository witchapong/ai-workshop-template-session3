"""Tests for core/triage.py. None of them call the real model.

Each test hands triage() a fake `ask` function that returns a fixed reply, so
the tests are free, instant, and give the same result on every run.

The import from core.triage sits inside each test on purpose. Before
core/triage.py exists, every test then fails on its own and pytest reports
"8 failed", instead of a single collection error that hides the count.
"""

import json

import pytest

GOOD = {
    "category": "order",
    "urgency": "low",
    "summary": "Wants two beige shirts in size M.",
    "draft_reply": "Thanks! Two beige shirts in M are on their way.",
}


def fake_model(**changes):
    """A fake model that always returns GOOD, with any fields changed."""
    answer = {**GOOD, **changes}
    return lambda system, message: json.dumps(answer)


def test_reply_fields_come_through():
    from core.triage import triage
    assert triage("two beige shirts in M", ask=fake_model()) == GOOD


def test_complaint_high_needs_you():
    from core.triage import next_action, triage
    result = triage("where is my order", ask=fake_model(category="complaint", urgency="high"))
    assert next_action(result) == "needs_you"


def test_complaint_not_high_gets_a_reply():
    from core.triage import next_action, triage
    result = triage("the shirt is a bit small", ask=fake_model(category="complaint", urgency="medium"))
    assert next_action(result) == "reply"


def test_other_is_ignored():
    from core.triage import next_action, triage
    result = triage("you won an iPhone", ask=fake_model(category="other"))
    assert next_action(result) == "ignore"


def test_invalid_json_is_unreadable():
    from core.triage import UnreadableAnswer, triage
    with pytest.raises(UnreadableAnswer):
        triage("hello", ask=lambda system, message: "Sure! It is an order.")


def test_missing_field_is_unreadable():
    from core.triage import UnreadableAnswer, triage
    no_urgency = {key: value for key, value in GOOD.items() if key != "urgency"}
    with pytest.raises(UnreadableAnswer):
        triage("hello", ask=lambda system, message: json.dumps(no_urgency))


def test_unknown_category_is_unreadable():
    from core.triage import UnreadableAnswer, triage
    with pytest.raises(UnreadableAnswer):
        triage("hello", ask=fake_model(category="refund"))


def test_busy_model_raises_busy():
    from core.triage import ModelBusy, triage

    def busy(system, message):
        raise ModelBusy("The model is busy.")

    with pytest.raises(ModelBusy):
        triage("hello", ask=busy)
