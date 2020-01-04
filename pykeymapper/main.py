import sys
from ctypes import *

from .events import CODE, VALUE, TYPE, InputEvent
from .logging import log
from .utils import push_key, write_event


class Modifier:
    code = None
    mapping = {}

    def __init__(self):
        self.is_space_down = False
        self.is_actual = True

    def is_modifier_key(self, input_event):
        return input_event.code == self.code

    def handle_mod_key_input(self, input_event):
        if input_event.value == VALUE.KEY_DOWN:
            self.is_space_down = True
            self.is_actual = True

        if input_event.value == VALUE.KEY_UP:
            self.is_space_down = False
            if self.is_actual:
                push_key(input_event.code)

    def handle_other_input(self, input_event):

        if not self.is_space_down:
            write_event(input_event)
        elif input_event.value == VALUE.KEY_DOWN:
            self.is_actual = False
            default_callback = lambda: push_key(input_event.code)
            callback_function = self.mapping.get(input_event.code, default_callback)
            callback_function()

    def handle_input(self, input_event):
        if self.is_modifier_key(input_event):
            self.handle_mod_key_input(input_event)
        else:
            self.handle_other_input(input_event)


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
