#!/usr/bin/env python
import clipboard
import webbrowser
from pykeyboard import PyKeyboard
import time

k = PyKeyboard()

time.sleep(0.2)

k.press_key(k.control_key)
k.tap_key("c")
k.release_key(k.control_key)

text = clipboard.paste()

webbrowser.open('https://en.oxforddictionaries.com/definition/%s' % (text))



