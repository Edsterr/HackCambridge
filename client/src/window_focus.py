import Xlib.display
import asyncio
import datetime
class TimeDelta(datetime.timedelta):
    def __str__(self):
        return "%s%s%s"%(
            self.hour + "h",
            self.minute + "m",
            self.second + "s"
        )
    def __repr__(self):
        return self.__str_()
datetime.timedelta = TimeDelta
print(datetime.timedelta)
class Session:
    def __init__(self):
        self.display = Xlib.display.Display()
        self.focus_log = {}
        self.current_focus = None
        self.time_prev = None
    
    def get_focus(self):
        window = self.display.get_input_focus().focus
         
        wmname = window.get_wm_name()
        wmclass = window.get_wm_class()
    
        if wmclass is None and wmname is None:
            window = window.query_tree().parent
            wmname = window.get_wm_name()
    
        return wmname

    def update_focus(self):
        window_name = self.get_focus()
        time_now = datetime.datetime.now()
        if self.current_focus == window_name:
            delta_time = time_now - self.time_prev
            self.focus_log[window_name] = self.focus_log.get(window_name,datetime.timedelta(0)) + delta_time
        else:
            self.current_focus = window_name
            
        self.time_prev = time_now

        



async def run():
    session = Session()
     
    while(True):
        session.update_focus()
        await asyncio.sleep(0.5)
        print("Log: %s"%(str(session.focus_log ))


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
