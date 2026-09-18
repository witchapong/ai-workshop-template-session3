"""Customer inbox triage: one message in, four fields and a decision out.

The model turns a messy message into fields. What to do about those fields is
decided by plain Python in next_action(), so it can be tested without the model.
"""

import json
import os
import random
import time
import urllib.error
import urllib.request
from pathlib import Path

from dotenv import load_dotenv

ZAI_URL = "https://api.z.ai/api/coding/paas/v4/chat/completions"
ZAI_MODEL = "glm-5.3-flash"
RETRY_WAITS = (2, 4, 8)  # seconds to wait before each retry after a 429
CATEGORIES = ("order", "complaint", "question", "other")
URGENCIES = ("low", "medium", "high")
FIELDS = ("category", "urgency", "summary", "draft_reply")

SYSTEM_PROMPT = (
    "You triage customer messages for a small online clothing shop. "
    "Reply with JSON only, using exactly these keys: "
    '"category" (one of "order", "complaint", "question", "other"), '
    '"urgency" (one of "low", "medium", "high"), '
    '"summary" (one sentence), and '
    '"draft_reply" (two or three friendly sentences, in the same language the '
    'customer wrote in). Use "other" for spam or anything that is not a real '
    "customer message."
)


class ModelBusy(Exception):
    """The model could not be reached, or was still busy after every retry."""


class UnreadableAnswer(Exception):
    """The model replied, but not in the shape that was asked for."""


def ask_zai(system: str, message: str) -> str:
    """Send one message to the model and return the text of its reply.

    When the model answers 429 (too many requests), wait 2, then 4, then 8
    seconds, plus up to one random second each time, and try again. After the
    last retry, give up with ModelBusy.
    """
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
    key = os.environ.get("ZAI_API_KEY", "").strip()
    body = json.dumps({
        "model": ZAI_MODEL,
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": message}],
        "response_format": {"type": "json_object"},
        "thinking": {"type": "disabled"},
        "max_tokens": 800,
    }).encode()
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}

    for attempt in range(len(RETRY_WAITS) + 1):
        request = urllib.request.Request(ZAI_URL, data=body, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                raw = response.read()
        except urllib.error.HTTPError as error:
            if error.code == 429 and attempt < len(RETRY_WAITS):
                time.sleep(RETRY_WAITS[attempt] + random.random())
                continue
            if error.code == 429:
                raise ModelBusy("The model is busy.") from error
            raise ModelBusy(
                f"The model refused the request (HTTP {error.code}). Run check_setup.py."
            ) from error
        except (urllib.error.URLError, TimeoutError) as error:
            raise ModelBusy("Could not reach the model.") from error
        try:
            return json.loads(raw)["choices"][0]["message"]["content"]
        except (ValueError, KeyError, IndexError, TypeError) as error:
            raise UnreadableAnswer("The reply was not in the expected form.") from error
    raise ModelBusy("The model is busy.")


def triage(message: str, ask=ask_zai) -> dict:
    """Ask the model to triage one message; return its four fields, checked.

    `ask` is the function that talks to the model. The app uses the real one;
    tests pass a fake that returns a fixed reply.
    """
    raw = ask(SYSTEM_PROMPT, message)
    try:
        answer = json.loads(raw)
    except (ValueError, TypeError) as error:
        raise UnreadableAnswer("The answer was not JSON.") from error
    if not isinstance(answer, dict) or any(field not in answer for field in FIELDS):
        raise UnreadableAnswer("The answer was missing a field.")
    if answer["category"] not in CATEGORIES or answer["urgency"] not in URGENCIES:
        raise UnreadableAnswer("The answer used a category or urgency we do not allow.")
    return {field: answer[field] for field in FIELDS}


def next_action(result: dict) -> str:
    """Decide what the shop owner should do about one triaged message.

    Plain Python, no model: "needs_you" for a high-urgency complaint, "ignore"
    for anything that is not a real customer message, "reply" otherwise.
    """
    if result["category"] == "complaint" and result["urgency"] == "high":
        return "needs_you"
    if result["category"] == "other":
        return "ignore"
    return "reply"
