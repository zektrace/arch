from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run_health_server():
    server = HTTPServer(('0.0.0.0', 8080), HealthHandler)
    server.serve_forever()

Thread(target=run_health_server, daemon=True).start()
