from pykeymapper.events import VALUE
from pykeymapper.utils import push_key, write_event, make_key_event


class Modifier:
    code = None
    release_code = None
    mapping = {}

    def __init__(self):
        self.is_mod_down = False
        self.is_actual = True
        self.unreleased_keys = set([])

    def release_keys(self):
        for code in self.unreleased_keys:
            write_event(make_key_event(code, VALUE.KEY_UP))

    def is_modifier_key(self, input_event):
        return input_event.code == self.code

    def get_release_code(self):
        return self.release_code or self.code

    def handle_mod_key_input(self, input_event):
        if input_event.value == VALUE.KEY_DOWN:
            self.release_keys()
            self.is_mod_down = True
            self.is_actual = True

        if input_event.value == VALUE.KEY_UP:
            self.is_mod_down = False
            if self.is_actual:
                push_key(self.get_release_code())

    def handle_other_input(self, input_event):
        if not self.is_mod_down:
            write_event(input_event)

            if input_event.value == VALUE.KEY_DOWN:
                self.unreleased_keys.add(input_event.code)
            if input_event.value == VALUE.KEY_UP:
                try:
                    self.unreleased_keys.remove(input_event.code)
                except KeyError:
                    pass

        elif input_event.value in [VALUE.KEY_DOWN, VALUE.KEY_REPEAT]:
            self.is_actual = False
            try:
                callback_function = self.mapping[input_event.code]
            except KeyError:
                callback_function = lambda input_event_code: push_key(input_event_code)

            callback_function(input_event.code)

    def handle_input(self, input_event):
        if self.is_modifier_key(input_event):
            self.handle_mod_key_input(input_event)
        else:
            self.handle_other_input(input_event)
