from http.server import BaseHTTPRequestHandler, HTTPServer
from nortia.repo import read_all
from nortia.calchours import calc_hours


def format_output(all_entries):
    text = ""
    for day, entries in all_entries.items():
        row = calc_hours(entries)
        text += day+"\t" + "\t".join(row)
    return text


def web_srv_class_factory(csv_filename):
    class CsvServerHandler(BaseHTTPRequestHandler):
        # pylint: disable=invalid-name
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            all_entries = read_all(csv_filename)
            self.wfile.write(bytes(format_output(all_entries), "utf-8"))

    return CsvServerHandler


def serve(filename):
    port = 8000
    server_address = ('', port)
    print(f"HTTP listening at {port}")
    handler_cls = web_srv_class_factory(filename)
    httpd = HTTPServer(server_address, handler_cls)
    httpd.serve_forever()
