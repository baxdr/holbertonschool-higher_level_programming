import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    Simple API handler using http.server.
    Handles GET requests for '/', '/data', '/status', and undefined endpoints.
    """

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(
                b"Hello, this is a simple API!"
            )

        elif self.path == '/data':
            sample = {'name': 'John', 'age': 30, 'city': 'New York'}
            payload = json.dumps(sample).encode('utf-8')

            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

        elif self.path == '/status':
            status = {'status': 'OK'}
            payload = json.dumps(status).encode('utf-8')

            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

        else:
            message = b"Endpoint not found"
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.send_header('Content-Length', str(len(message)))
            self.end_headers()
            self.wfile.write(message)


def run_server(port=8000):
    """
    Starts the HTTP server on the given port.
    """
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Starting server on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        print("Server stopped.")


if __name__ == '__main__':
    run_server(8000)
