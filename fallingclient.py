from websockets.sync.client import connect

class FallingClient:

    def __init__(self, serverAddress):
        self.websocket = connect(serverAddress)
        self.websocket.send("Hello world!")


    def recv(self):
        message = self.websocket.recv()
        print(message)
        # interpret the message here, return enum value.


    def disconnect(self):
         self.websocket.close(1000)