
import sys
import json
import asyncio
import datetime
import random
import websockets
import base64
import pickle

# adapted with love from
# https://websockets.readthedocs.io/en/stable/intro.html

# Create basic event object

# title

# description

# various options (each a button)
#  each button sends a different command to the server

# option should have text and then a command to send back to the server
# (is a list of tuples)

# event should also have a type so that the client knows what to do with it
class BasicEvent:
    def __init__(self,title="",description="",image_bytes=None,options=[("exit","choice","exit")]):
        self.title=title
        self.description=description
        self.options=options
        self.type="BasicEvent"
        self.image=image_bytes
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    
# def CreateInputBox(self,input_type):
    # d={}
    # d['type']=input_type
    # if(input_type=="text"):
        # d[']
    
# class EditMode:
    # def __init__(self,type):
        # if(type=="BasicEvent"):
            
            
            
            
# ability to save events via pickle
# also list of all events

def encodeImage(image_file):
    encoded = base64.b64encode(open(image_file, "rb").read())
    return str('data:image/png;base64,{}'.format(encoded.decode()))

op=[("a","choice","You chose a"),
("b","choice","You chose b"),
("c","choice","You chose c")]

be=BasicEvent("Event Title",
open('lorem.txt').read(),
encodeImage('test.jpg'),
op)

EventList=[]

def createEvent(title,text,image,op):
    ev=BasicEvent(title,text,image,op)
    EventList.append(ev)
    return ev

    # save everytime an event is created or changed by an edit mode user
def saveEvents(e_list):
    # we'll replace this later with the name of the campaign/universe and a timestamp
    pickle.dump(e_list, open("event_save.p","wb"))

    # load when the server starts up
def loadEvents(save_file):
    return pickle.load(open(save_file,"rb"))
    
def randomlist():
    l=[]
    for x in range(0,random.randint(1,10)):
        l.append(random.randint(0,100))
    return l

def save_http_headers(ws):
    # i want to inspect the headers so I can see if theres a session variable in there
    # i can use to identify different users
    ws_key=ws.request_headers['sec-websocket-key']
    file=open("headers/"+ws_key+".txt","w")
    for entry in ws.request_headers:
        file.write(str(entry)+" "+ ws.request_headers[entry] +"\n")
    file.close()
    
    # ok so
    # websocket.request_headers['sec-websocket-key']
    # is our unique session identifier
    
USERS = set()
    
async def register(websocket): 
    USERS.add(websocket)

async def unregister(websocket):
    USERS.remove(websocket)

    
# so i think this function runs for each user?
async def mainloop(websocket, path):

    # save_http_headers(websocket)
    await register(websocket)
    try:
        async for message in websocket:
            data = json.loads(message)
            if data['action']=='newlist':
                await websocket.send(json.dumps(randomlist()))
            if data['action']=='newevent':
                await websocket.send(json.dumps(be.toJSON()))
            if data['action']=='choice':
                await websocket.send(json.dumps(createEvent(title=data['new_event']).toJSON()))
    finally:
        await unregister(websocket)


start_server = websockets.serve(mainloop, "",5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()