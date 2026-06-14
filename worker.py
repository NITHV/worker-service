import json
import logging
import os
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/health":
            self.send_response(404)
            self.end_headers()
            return

        body = json.dumps({"status": "ok", "service": "worker"}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *_):
        return


def run_health_server():
    port = int(os.getenv("PORT", "9090"))
    ThreadingHTTPServer(("127.0.0.1", port), HealthHandler).serve_forever()


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    threading.Thread(target=run_health_server, daemon=True).start()
    logging.info("worker started")
    while True:
        logging.info("worker heartbeat")
        time.sleep(30)


if __name__ == "__main__":
    main()
