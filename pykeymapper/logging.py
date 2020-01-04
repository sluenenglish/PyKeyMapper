import sys
import time


def log(text):
    print(str(text), file=sys.stderr)


def log_event(input_event, extra=""):
    if input_event.code == 0:
        return
    message = f"""

---{extra}  {time.time()}
Code: {input_event.code}
Value: {input_event.value}
Type: {input_event.type}
---

    """
    log(message)
