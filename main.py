import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open("contacts.html", "rb") as f:
                html_content = f.read()
            self.wfile.write(html_content)
        elif self.path.startswith('/css/'):
            file_path = os.path.join('css', self.path[5:])
            with open(file_path, 'rb') as file:
                content = file.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/css')
                self.end_headers()
                self.wfile.write(content)
        else:
            self.send_error(404, "File Not Found")

def run_server():
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print("Сервер запущен на http://127.0.0.1:8000")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()