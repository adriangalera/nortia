# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from nortia.repo import read_all


def MakeHandlerClassFromArgv(csv_filename):
    class CustomHandler(BaseHTTPRequestHandler):

        def __init__(self, *args, **kwargs):
            super(CustomHandler, self).__init__(*args, **kwargs)

        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            all_entries = read_all(csv_filename)
            self.wfile.write(bytes(json.dumps(all_entries), "utf-8"))

    return CustomHandler


def serve(filename):
    server_address = ('', 8000)
    HandlerClass = MakeHandlerClassFromArgv(filename)
    httpd = HTTPServer(server_address, HandlerClass)
    httpd.serve_forever()
