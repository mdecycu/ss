import http.server
import socketserver

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # 注入啟用 WebAssembly 共享記憶體必備的安全標頭
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()

# 確保 .wasm 檔的 MIME 類型正確
MyHTTPRequestHandler.extensions_map.update({
    '.wasm': 'application/wasm',
})

print(f"伺服器已成功啟動：http://localhost:{PORT}")
with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    httpd.serve_forever()
