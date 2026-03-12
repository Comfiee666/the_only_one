import http.server
import socketserver
from http.server import HTTPServer
httpd = socketserver.TCPServer(("", 1228), http.server.SimpleHTTPRequestHandler)
httpd.serve_forever()