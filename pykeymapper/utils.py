import logging

import sys

from pykeymapper.events import InputEvent, TYPE, VALUE

logger = logging.getLogger(__name__)


def write_event(event):
    logger.debug(f"Writing event: {str(event)}")
    sys.stdout.buffer.write(event)
    sys.stdout.buffer.flush()


def make_key_event(code, value, type=None):
    event = InputEvent()
    event.code = code
    event.value = value
    event.type = type or TYPE.EV_KEY
    return event


def push_key(code, modifiers=None):

    if modifiers is None:
        modifiers = []

    for mod_code in modifiers:
        write_event(make_key_event(mod_code, VALUE.KEY_DOWN))

    write_event(make_key_event(code, VALUE.KEY_DOWN))
    write_event(make_key_event(code, VALUE.KEY_UP))

    for mod_code in modifiers:
        write_event(make_key_event(mod_code, VALUE.KEY_UP))
