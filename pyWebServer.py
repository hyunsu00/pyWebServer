# pyWebServer.py

from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
from functools import partial
from pathlib import Path
import socket

def main(host : str = "0.0.0.0", port : int = 8080, webDirs : Path = os.path.join(os.path.dirname(__file__), 'public')):
    with HTTPServer((host, port), partial(SimpleHTTPRequestHandler, directory=webDirs)) as httpd:
        print("running")
        print(httpd)
        print("Local:            http://localhost:" + str(port));
        print("On Your Network:  http://" + socket.gethostbyname(socket.gethostname()) + ":" + str(port))
        httpd.serve_forever()

if __name__ == "__main__":
    main()