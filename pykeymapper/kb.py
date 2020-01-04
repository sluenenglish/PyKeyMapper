import sys
from ctypes import sizeof

from pykeymapper.events import CODE, VALUE, TYPE, InputEvent
from pykeymapper.input_modifier import Modifier
from pykeymapper.logging import log
from pykeymapper.utils import write_event, push_key


class SpaceModifier(Modifier):
    code = CODE.KEY_SPACE
    mapping = {
        CODE.KEY_Q: lambda: push_key(CODE.KEY_SLASH, modifiers=[CODE.KEY_LEFTSHIFT]),
        CODE.KEY_W: lambda: push_key(CODE.KEY_MINUS),
        CODE.KEY_E: lambda: push_key(CODE.KEY_EQUAL),
        CODE.KEY_R: lambda: push_key(CODE.KEY_EQUAL, modifiers=[CODE.KEY_LEFTSHIFT]),
        CODE.KEY_O: lambda: push_key(CODE.KEY_GRAVE, modifiers=[CODE.KEY_LEFTSHIFT]),
        CODE.KEY_P: lambda: push_key(
            CODE.KEY_BACKSLASH, modifiers=[CODE.KEY_LEFTSHIFT]
        ),
        CODE.KEY_D: lambda: push_key(
            CODE.KEY_APOSTROPHE, modifiers=[CODE.KEY_LEFTSHIFT]
        ),
        CODE.KEY_F: lambda: push_key(CODE.KEY_APOSTROPHE),
        CODE.KEY_U: lambda: push_key(CODE.KEY_MINUS, modifiers=[CODE.KEY_LEFTSHIFT]),
    }


def main():
    input_event = InputEvent()

    space_mod = SpaceModifier()
    paused = False
    while sys.stdin.buffer.readinto(input_event) == sizeof(input_event):

        if input_event.type == TYPE.EV_MSC and input_event.code == CODE.MSC_SCAN:
            continue

        if input_event.type != TYPE.EV_KEY:
            write_event(input_event)
            continue

        if input_event.code == CODE.KEY_PAUSE and input_event.value == VALUE.KEY_DOWN:
            continue
        if input_event.code == CODE.KEY_PAUSE and input_event.value == VALUE.KEY_UP:
            paused = not paused
            log("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            continue

        if paused:
            write_event(input_event)
            continue

        space_mod.handle_input(input_event)


if __name__ == "__main__":
    main()
