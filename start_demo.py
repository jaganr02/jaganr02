import http.server
import socketserver
import webbrowser
import os
import sys

# Ensure UTF-8 output encoding
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8')

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        sys.stderr.write(f"[DEMO SERVER] {self.address_string()} - {format%args}\n")

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print("========================================================")
        print(">>> R JAGAN - GITHUB PROFILE LIVE DEMO SERVER RUNNING")
        print(f">>> Local URL: {url}")
        print(f">>> Directory: {DIRECTORY}")
        print(">>> Press Ctrl+C in terminal to stop server")
        print("========================================================")
        
        try:
            webbrowser.open(url)
        except Exception:
            pass
            
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            httpd.server_close()
