import asyncio
from session import *
import json
import requests

import config

async def send_data(session):
    while(True):
        response = requests.post(config.post_url, json={
            "focus_log":session.focus_log,
            "kb_activity":session.kb_activity,
            "username":config.username,
            "password":config.password
        })
        await asyncio.sleep(60)

async def run():
    session = create_session()
     
    asyncio.ensure_future(send_data(session))
    while True:
        await session.update_focus()
        await asyncio.sleep(1.0)
        print("Log: %s"%(str(session.focus_log)) )
        print(session.kb_activity)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())

# ls
