'''
Created on 2011-09-22

@author: Alec
'''
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
from threading import Thread

#We are using threads instead of subprocesses because of http://bugs.python.org/issue11969
class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass

DEFAULT_ADDRESS = ("127.0.0.1", 8080) 
DEFAULT_STATUS = 200
DEFAULT_HEADERS = {"Content-type": "text/html"}
DEFAULT_BODY = "A-OK!"

def serve_in_a_thread(server):
    server.serve_forever()
    

class EchoServer(object):
    """A simple HTTP server that allows you to set a response to return to 
    every request."""
    
    
    def __init__(self, server_address):
        self.server_address = server_address
        self.set_echo()
    
    
    def set_echo(self, status=DEFAULT_STATUS, headers=DEFAULT_HEADERS, 
                 body=DEFAULT_BODY):
        """Set the echo response for this server."""
        class EchoHandler(BaseHTTPRequestHandler):
            wfile = None #This is required to successfully mock this out
            def do_GET(self):
                self.send_response(status)
                for key, value in headers.items():
                    self.send_header(key, value)
                self.end_headers()
                self.wfile.write(body)
        
        self.RequestHandlerClass = EchoHandler


    def threaded_serve(self):
        """Start another process to serve this."""
        self.server = ThreadingHTTPServer(self.server_address, 
                                          self.RequestHandlerClass)
        self.thread = Thread(target=serve_in_a_thread, args=(self.server, ))
        self.thread.start()
        
        
    def threaded_shutdown(self):
        self.server.shutdown()
        self.thread.join()

        
                
if __name__ == "__main__":
    server = EchoServer(DEFAULT_ADDRESS)
    server.threaded_serve()
    raw_input("Serving, press enter to terminate")
    server.threaded_shutdown()
    print("All done")
