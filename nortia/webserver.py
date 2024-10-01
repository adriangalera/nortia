from urllib.parse import unquote
from http.server import BaseHTTPRequestHandler, HTTPServer
from nortia.repo import read_all, replace
from nortia.calchours import calc_hours


def format_output(all_entries):
    text = ""
    for day, entries in all_entries.items():
        row = calc_hours(entries)
        text += day + "\t" + "\t".join(row)+"\n"
    return text


def web_srv_class_factory(csv_filename):
    class CsvServerHandler(BaseHTTPRequestHandler):
        # pylint: disable=invalid-name
        def do_GET(self):
            content = None
            if "/replace/" in self.path:
                sp = self.path.split("/")
                search_str = unquote(sp[-2])
                replace_str = unquote(sp[-1])
                content = replace(csv_filename, search_str, replace_str)
                content = format_output(content)
            else:
                all_entries = read_all(csv_filename)
                content = format_output(all_entries)

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(bytes(content, "utf-8"))

    return CsvServerHandler


def serve(filename):
    port = 8000
    server_address = ('', port)
    print(f"HTTP listening at {port}")
    handler_cls = web_srv_class_factory(filename)
    httpd = HTTPServer(server_address, handler_cls)
    httpd.serve_forever()
