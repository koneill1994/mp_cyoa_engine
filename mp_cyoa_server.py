print(-1)

import sys
import json
import asyncio
import datetime
import random
import websockets


# Create basic event object

# title

# description

# various options (each a button)
#  each button sends a different command to the server

# option should have text and then a command to send back to the server
# (is a list of tuples)

class BasicEvent:
    def __init__(self,title,description,options):
        self.title=title
        self.description=description
        self.options=options
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    

op=[("a","choice","You chose a"),
("b","choice","You chose b"),
("c","choice","You chose c")]

be=BasicEvent("Event Title",
"Event Description",
op)

def createEvent(text):
    return BasicEvent("Event Title",text,op)

def randomlist():
    l=[]
    for x in range(0,random.randint(1,10)):
        l.append(random.randint(0,100))
    return l


async def time(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        if data['action']=='newlist':
            await websocket.send(json.dumps(randomlist()))
        if data['action']=='newevent':
            await websocket.send(json.dumps(be.toJSON()))
        if data['action']=='choice':
            await websocket.send(json.dumps(createEvent(data['new_event']).toJSON()))

start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()