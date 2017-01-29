import asyncio
from session import *
import json
import requests

import config
def datetime_handler(x):
    if isinstance(x, datetime.timedelta):
        return str(x)
    return str(x)

async def server_login(session):
    json_data = json.dumps({"username":config.username, "password":config.password})
    response = requests.post(config.post_url + "/login/")  
    
 
async def send_data(session):
    while(True):
        json_data = json.dumps({
            "focus_log":session.focus_log,
            "kb_activity":session.kb_activity,
            "username":config.username,
            "password":config.password
        }, default = datetime_handler)
        response = requests.post(config.post_url + "/productivity/addrecord/",data=json_data, headers={"Content-type":"application/json","Accept":"text/plain"} )
        await asyncio.sleep(10)

async def run():
    session = create_session()
    await server_login(session) 
    asyncio.ensure_future(send_data(session))
    while True:
        await session.update_focus()
        await asyncio.sleep(1.0)
        #print("Log: %s"%(str(session.focus_log)) )
        #print(session.kb_activity)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())

# ls
