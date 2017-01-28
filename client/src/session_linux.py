import Xlib.display
from session import *

class SessionLinux(Session):
    def __init__(self, **kwargs):
        self.display = Xlib.display.Display()
        Session.__init__(self) 

    def get_focus(self):
        window = self.display.get_input_focus().focus
         
        wmname = window.get_wm_name()
        wmclass = window.get_wm_class()
    
        if wmclass is None and wmname is None:
            window = window.query_tree().parent
            wmname = window.get_wm_name()
    
        return wmname

