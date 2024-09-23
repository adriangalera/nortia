# Python 3 server example
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer


def MakeHandlerClassFromArgv(csv_filename):
    class CustomHandler(BaseHTTPRequestHandler):

        def __init__(self, *args, **kwargs):
            super(CustomHandler, self).__init__(*args, **kwargs)

        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            with open(csv_filename, 'r', encoding='utf-8') as fp:
                self.wfile.write(bytes(fp.read(), 'utf-8'))

    return CustomHandler


def serve(filename):
    server_address = ('', 8000)
    HandlerClass = MakeHandlerClassFromArgv(filename)
    httpd = HTTPServer(server_address, HandlerClass)
    httpd.serve_forever()
