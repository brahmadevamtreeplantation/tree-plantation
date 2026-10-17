from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit


SITE_DIRECTORY = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = 8000


class TreePlantationHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(SITE_DIRECTORY), **kwargs)

    def do_GET(self):
        path = urlsplit(self.path).path

        if path == "/":
            self.path = "/index.html"
        elif path not in {"/index.html", "/about.html", "/green-oasis.html"}:
            self.send_error(404, "Page not found")
            return

        super().do_GET()


def main():
    server = ThreadingHTTPServer((HOST, PORT), TreePlantationHandler)
    print(f"Team Green website is running at http://{HOST}:{PORT}")
    print("Press Ctrl+C to stop the server.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping the website server.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
