import http.server
import webbrowser
import threading
import os

PORT = 8080
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def open_browser():
    webbrowser.open(f"http://localhost:{PORT}")

threading.Timer(0.5, open_browser).start()

print(f"Servidor rodando em http://localhost:{PORT}")
print("Pressione Ctrl+C para parar.")

http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=PORT, bind="localhost")
