import SocketServer
import socket

class MyHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        while 1:
            try:
                dataReceived = self.request.recv(1024)
                if not dataReceived: break
                else:
                    print(dataReceived)
                self.request.send('get %s'% dataReceived)
            except socket.timeout:
                print "caught socket.timeout exception"

    def setup(self):
        self.request.settimeout(60)
    def finish(self):
        self.request.close()

myServer = SocketServer.ThreadingTCPServer(('',9999), MyHandler)
myServer.serve_forever(  )

