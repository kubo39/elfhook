# coding: utf-8

import time
from SimpleHTTPServer import SimpleHTTPRequestHandler
import SocketServer

PORT = 9999
BLOCKING_SECONDS = 10  # seconds


class Server(SocketServer.TCPServer):
    allow_reuse_address = True


class Handler(SimpleHTTPRequestHandler):

    def do_HEAD(self):
        time.sleep(BLOCKING_SECONDS)
        return SimpleHTTPRequestHandler.do_HEAD(self)


if __name__ == '__main__':
    httpd = Server(("", PORT), Handler)
    try:
        httpd.serve_forever()
    except:
        httpd.server_close()
