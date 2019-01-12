#!/usr/bin/env python3

import clipboard
import webbrowser
from pynput.keyboard import Key, Controller
import time

k = Controller()

time.sleep(0.2)

with k.pressed(Key.ctrl):
    k.press('c')
    k.release('c')


text = clipboard.paste()

webbrowser.open('https://en.oxforddictionaries.com/definition/%s' % (text))



