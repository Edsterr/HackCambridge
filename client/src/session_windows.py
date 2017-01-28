from win32gui import GetWindowText, GetForegroundWindow
from session import *

class SessionWindows(Session):
    def __init__(self, **kwargs):
        Session.__init__(self)

    def get_focus(self):
        return GetWindowText(GetForegroundWindow())
