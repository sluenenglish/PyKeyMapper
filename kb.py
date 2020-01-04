import sys
from ctypes import sizeof

from pykeymapper.events import CODE, VALUE, TYPE, InputEvent
from pykeymapper.logging import log
from pykeymapper.main import SpaceModifier
from pykeymapper.utils import write_event


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
