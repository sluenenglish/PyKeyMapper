=====
Usage
=====

PyKeyMapper is designed to be used in an `interception tools`_  flow.

.. _`interception tools`: https://gitlab.com/interception/linux/tools/


Premade
-------
For example, to map backslash to shift when pressed in conjunction with another key
you would use the following configuration file for `udevmon`.

.. code-block:: yaml

    - JOB: >
            intercept -g $DEVNODE |
            pykeymapper backslash2shift |
            uinput -d $DEVNODE
      DEVICE:
        EVENTS:
          EV_KEY: [KEY_BACKSLASH]

To see available mappings:
    .. code-block:: shell

        pykeymapper --help


Making a macro modifier
-----------------------
PyKeyMapper can be used to make ordinary keys modifiers which trigger
macros when pressed in combination with another key.

Let's take a look at a simplified version of the `Special Space` modifier.

.. code-block:: shell

    from pykeymapper import CustomModifier, CODE, push_key, run_mapper

    class SpecialSpace(CustomModifier):
        code = CODE.KEY_SPACE
        macros = {
            CODE.KEY_Q: lambda input_event_code: push_key(
                CODE.KEY_SLASH, modifiers=[CODE.KEY_LEFTSHIFT]
            ),
        }

    run_mapper(premade.SpecialSpace)

Firstly we define a class which inherits from `CustomModifier`.
On this class we define 2 variables:

- code:
    This tells PyKeyMapper which key is to act as the modifier.
- macros:
    This dictionary defines a mapping of input event codes to keyboard macros.
    In this case we map the key Q to a function which triggers a sequence of
    key-presses resulting in a question mark
    (shift down -> slash down -> slash up -> shift up).

We can also optionally define a 3rd variable:

- release_code:
    This tells PyKeyMapper what key to send on the release of the modifier key
    (if no keys were pressed in conjunction with the modifier).
    For example, if you wanted the space key to act as the enter key on release.

So in summary, the script we created results in:

- Normal space key behaviour if not pressed in conjunction with another key.
- If pressed in conjunction with one of the defined mappings,
  it will trigger the defined macro, and not send the space key on release.
- If pressed in conjunction with a key not in the mappings,
  it send that key normally, and not send the space key on release.
