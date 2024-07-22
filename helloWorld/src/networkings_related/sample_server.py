import http.server
import socketserver


class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello World")


PORT = 8000
Haneler = MyRequestHandler

with socketserver.TCPServer(("", PORT), Haneler) as httpd:
    print(f"Server is running on PORT http://localhost:{PORT}")
    httpd.serve_forever()
