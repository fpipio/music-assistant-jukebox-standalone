#!/usr/bin/env python3
"""
Simple HTTP Server for Music Assistant Jukebox
Serves the standalone HTML file with CORS support
"""

import http.server
import socketserver
import os
from pathlib import Path

# Configurazione
PORT = 8000
DIRECTORY = Path(__file__).parent

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP Request Handler with CORS support"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)

    def end_headers(self):
        """Add CORS headers to all responses"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def do_OPTIONS(self):
        """Handle OPTIONS requests for CORS preflight"""
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        """Custom log format"""
        print(f"[{self.log_date_time_string()}] {format % args}")

def main():
    """Start the HTTP server"""

    # Verifica che il file HTML esista
    html_file = DIRECTORY / "jukebox-standalone.html"
    if not html_file.exists():
        print(f"[ERROR] File {html_file} non trovato!")
        return

    # Crea il server
    with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
        print("=" * 60)
        print("Music Assistant Jukebox Server")
        print("=" * 60)
        print(f"Directory: {DIRECTORY}")
        print(f"Server in ascolto su: http://localhost:{PORT}")
        print(f"Jukebox URL: http://localhost:{PORT}/jukebox-standalone.html")
        print("=" * 60)
        print("Ricorda di configurare i parametri nel file HTML!")
        print("Premi CTRL+C per fermare il server")
        print("=" * 60)
        print()

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n[STOP] Server fermato.")
            print("=" * 60)

if __name__ == "__main__":
    main()
