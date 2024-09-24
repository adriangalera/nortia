from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from nortia.repo import read_all


def web_srv_class_factory(csv_filename):
    class CsvServerHandler(BaseHTTPRequestHandler):
        # pylint: disable=invalid-name
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            all_entries = read_all(csv_filename)
            self.wfile.write(bytes(json.dumps(all_entries), "utf-8"))

    return CsvServerHandler


def serve(filename):
    server_address = ('', 8000)
    handler_cls = web_srv_class_factory(filename)
    httpd = HTTPServer(server_address, handler_cls)
    httpd.serve_forever()
