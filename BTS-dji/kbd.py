from pynput.keyboard import Key, Listener
from threading import *
from time import sleep

dict = {
    "'`'": 0, "'1'": 0, "'2'": 0, "'3'": 0, "'4'": 0, "'5'": 0, "'6'": 0, "'7'": 0, "'8'": 0, "'9'": 0, "'0'": 0,
    "'-'": 0, "'='": 0, "<Key.backspace: <8>>": 0,
    "<Key.tab: <9>>": 0, "'q'": 0, "'w'": 0, "'e'": 0, "'r'": 0, "'t'": 0, "'y'": 0, "'u'": 0, "'i'": 0, "'o'": 0,
    "'p'": 0, "'['": 0, "']'": 0, "'\\'": 0,
    "<Key.caps_lock: <20>>": 0, "'a'": 0, "'s'": 0, "'d'": 0, "'f'": 0, "'g'": 0, "'h'": 0, "'j'": 0, "'k'": 0,
    "'l'": 0, "';'": 0, "''": 0, "<Key.enter: <13>>": 1,
    "<Key.shift: <160>>": 0, "'z'": 0, "'x'": 0, "'c'": 0, "'v'": 0, "'b'": 0, "'n'": 0, "'m'": 0, "','": 0, "'.'": 0,
    "'/'": 0, "<Key.shift_r: <161>>": 1,
    "<Key.space: ' '>": 0,
    "'*'": 0, "<103>": 0, "<104>": 0, "<105>": 0, "'+'": 0, "<100>": 0, "<101>": 0,
    "<102>": 0, "<97>": 0, "<98>": 0, "<99>": 0, "<96>": 0, "<110>": 0,
    "<Key.up: <38>>": 0, "<Key.down: <40>>": 0, "<Key.left: <37>>": 0, "<Key.right: <39>>": 0,
    "<Key.esc: <27>>": 0
}

simp = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'backspace',
        'tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\',
        'caps lock', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'enter',
        'left shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'right shift',
        'space',
        '*', 'numpad 7', 'numpad 8', 'numpad 9', '+', 'numpad 4', 'numpad 5',
        'numpad 6', 'numpad 1', 'numpad 2', 'numpad 3', 'numpad 0', '.',
        'up arrow', 'down arrow', 'left arrow', 'right arrow',
        'escape'
        ]


def on_press(key):
    """
    Sets the key to 1 when pressed.
    :param key:
    :rtype: dict
    """
    global dict
    dict[repr(key)] = 1
    # print(str(repr(key)) + (str(dict[repr(key)])))


def on_release(key):
    """
    Sets the key to 0 when released.
    :param key:
    :rtype: dict
    """

    global dict
    dict[repr(key)] = 0
    # print(str(repr(key)) + (str(dict[repr(key)])))


def get_state(num):
    """
    Returns the state of all keys as a dictionary.

    :return: A dictionary of all keys and their states.
    :rtype: dict
    """
    global dict

    temp = list(dict.values())
    clean = {}
    for x in range(len(simp)):
        clean[simp[x]] = temp[x]

    return clean


def start():
    """
    Starts the keyboard listener as a separate thread.
    """

    t1 = Thread(target=main)
    t1.start()


def main():
    """
    Starts the keyboard listener.
    """

    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
