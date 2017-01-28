import datetime
import platform

class UnsupportedOSException(Exception):
    pass
class Session:
    def __init__(self,**kwargs):
        self.focus_log = {}
        self.current_focus = None
        self.time_prev = None

    def update_focus(self):
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
def create_session(**kwargs):
    if platform.system() == "Linux":
        return SessionLinux(**kwargs)
    elif platform.system() == "Windows":
        return SessionWindows(**kwargs) 
    else:
        raise UnsupportedOSException("Unsupported OS: %s"%(platform.system()))

