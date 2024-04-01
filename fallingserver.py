import asyncio
from websockets.server import serve

class FallingServer:

    async def echo(self, websocket):
        async for message in websocket:
            print("Received message: {0}".format(message))
            await websocket.send(message)

    async def main(self):
        async with serve(self.echo, "localhost", 8765):
            await asyncio.Future()  # run forever

server = FallingServer()
asyncio.run(server.main())