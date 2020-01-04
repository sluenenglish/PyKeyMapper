import sys
import time
from ctypes import *

from .vars import CODE, VALUE, TYPE, InputEvent

def log(text):
    print(str(text), file=sys.stderr)

def log_event(input_event, extra=''):
    if input_event.code == 0:
        return
    message = f'''

---{extra}  {time.time()}
Code: {input_event.code}
Value: {input_event.value}
Type: {input_event.type}
---

    '''
    log(message)


def write_event(event):
    log_event(event, 'write_event')
    sys.stdout.buffer.write(event)
    sys.stdout.buffer.flush()


def push_key(input_event):
    log_event(input_event, 'push_key')
    input_event.value = VALUE.KEY_DOWN
    write_event(input_event)
    input_event.value = VALUE.KEY_UP
    write_event(input_event)


class Modifier:
    code = None
    mapping = {
    }

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
                push_key(input_event)

    def handle_other_input(self, input_event):
        self.is_actual = False

        if self.is_space_down:
            new_code = self.mapping.get(input_event.code, input_event.code)
            input_event.code = new_code

        write_event(input_event)


    def handle_input(self, input_event):
        if self.is_modifier_key(input_event):
            self.handle_mod_key_input(input_event)
        else:
            self.handle_other_input(input_event)




class SpaceModifier(Modifier):
    code = CODE.KEY_SPACE
    mapping = {
        CODE.KEY_E: CODE.KEY_EQUAL,
        CODE.KEY_W: CODE.KEY_MINUS,
        CODE.KEY_F: CODE.KEY_APOSTROPHE,

    }


def main():
    input_event = InputEvent()

    space_mod = SpaceModifier()
    while sys.stdin.buffer.readinto(input_event) == sizeof(input_event):

        if input_event.type == TYPE.EV_MSC and input_event.code == CODE.MSC_SCAN:
            continue

        if input_event.type != TYPE.EV_KEY:
            write_event(input_event)
            continue


        if input_event.code == CODE.KEY_1:
            exit(1)
        if input_event.code == CODE.KEY_2:
            log('\n\n\n\n\n\n\n')
            continue

        # write_event(input_event)

        space_mod.handle_input(input_event)
        log(f'is space down: {space_mod.is_space_down}')
        log(f'is actual: {space_mod.is_actual}')

        log('*********************')

