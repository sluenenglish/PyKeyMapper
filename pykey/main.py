"""
struct { double v; int t; char c;};
"""
import sys
import time
from ctypes import *
from io import BytesIO

from .vars import CODE, VALUE, TYPE


class TimeVal(Structure):
    _fields_ = [
        ('time', c_long),
        ('msec', c_long),
    ]


class InputEvent(Structure):
    _fields_ = [
        ('time', TimeVal),
        ('type', c_short),
        ('code', c_short),
        ('value', c_int),
    ]


event_path = '/home/sam/CLionProjects/keyboard_mapping/cmake-build-debug/file.dat'

sync_event = InputEvent(type=TYPE.EV_SYN, value=VALUE.KEY_UP, code= CODE.SYN )

def write_event(event):
    sys.stdout.buffer.write(event)
    sys.stdout.buffer.flush()


def main():
    input_event = InputEvent()
    while sys.stdin.buffer.readinto(input_event) == sizeof(input_event):
        write_event(input_event)

        if input_event.code == CODE.KEY_SPACE and input_event.value == VALUE.KEY_UP:
            input_event.value = VALUE.KEY_DOWN
            write_event(input_event)

            input_event.value = VALUE.KEY_UP
            write_event(input_event)
