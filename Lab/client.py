import asyncio
import websockets
import json
import sys

async def start():
    uri = "ws://172.16.100.153:6666"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"pin":sys.argv[1],"time":sys.argv[2]}))
        
asyncio.get_event_loop().run_until_complete(start())
