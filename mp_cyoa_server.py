print(-1)

import sys
import json
import asyncio
import datetime
import random
import websockets

print(0)

def randomlist():
    l=[]
    for x in range(0,random.randint(1,10)):
        l.append(random.randint(0,100))
    return l

print(1)
    
list1=randomlist()
    
print(list1)
print(json.dumps(randomlist()))
    

async def time(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        if data['action']=='newlist':
            await websocket.send(json.dumps(randomlist()))

start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()