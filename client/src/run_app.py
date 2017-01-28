import asyncio
from session import *

async def run():
    session = create_session()
     
    while(True):
        session.update_focus()
        await asyncio.sleep(0.5)
        print("Log: %s"%(str(session.focus_log )) )

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
