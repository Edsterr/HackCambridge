import asyncio
from session import *

async def run():
    session = create_session()
     
    while True:
        await session.update_focus()
        await asyncio.sleep(0.25)
        print("Log: %s"%(str(session.focus_log )) )
        print(session.kb_activity)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
