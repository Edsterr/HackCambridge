import datetime
import platform

import pyxhook
import time

class UnsupportedOSException(Exception):
    pass
class Session:
    def __init__(self,**kwargs):
        self.focus_log = {}
        self.current_focus = None
        self.time_prev = None

        self.kb_activity = []
        self.kb_listener = pyxhook.HookManager()
        self.kb_listener.KeyDown = self.on_press
        self.kb_listener.HookKeyboard()
        self.kb_listener.start()
    

    def on_press(self, event):
        self.kb_activity.append(event.__dict__)

    async def update_focus(self):
        window_name = self.get_focus()
        time_now = datetime.datetime.now()
        if self.current_focus == window_name:
            delta_time = time_now - self.time_prev
            self.focus_log[window_name] = self.focus_log.get(window_name,datetime.timedelta(0)) + delta_time
        else:
            self.current_focus = window_name
            
        self.time_prev = time_now


if platform.system() == "Linux":
    from session_linux import *
elif platform.system() == "Windows":
    from session_windows import *
def create_session(**kwargs):
    if platform.system() == "Linux":
        return SessionLinux(**kwargs)
    elif platform.system() == "Windows":
        return SessionWindows(**kwargs) 
    else:
        raise UnsupportedOSException("Unsupported OS: %s"%(platform.system()))

