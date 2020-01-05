from pykeymapper.events import VALUE
from pykeymapper.utils import push_key, write_event


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
