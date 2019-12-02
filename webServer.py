import os
import http.server
import socketserver
import threading

PORT = 8080
DIRECTORY = os.getcwd() + '\\mapfile'


class WebServer():
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=DIRECTORY, **kwargs)

    def __init__(self):
        self.httpd = socketserver.TCPServer(("", PORT), self.Handler)
        self.server_thread = threading.Thread(target=self.httpd.serve_forever)
        self.server_thread.daemon = True

    def startServer(self):
        self.server_thread.start()

    def stopServer(self):
        self.httpd.shutdown()
        self.httpd.server_close()


if __name__ == '__main__':
    webserver = WebServer()
    webserver.startServer()
    print("running...")
    input()