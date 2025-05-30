from http.server import BaseHTTPRequestHandler, HTTPServer
import time

# 自定义请求处理类
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # 定义HTML内容
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Pure Python Web Server</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                    text-align: center;
                    padding: 50px;
                }
                h1 {
                    color: #2c3e50;
                }
                p {
                    color: #7f8c8d;
                }
            </style>
        </head>
        <body>
            <h1>Hello from Pure Python!</h1>
            <p>Server time: %s</p>
        </body>
        </html>
        """ % time.ctime()

        # 设置响应头
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # 返回HTML内容
        self.wfile.write(html_content.encode("utf-8"))

if __name__ == "__main__":
    # 配置服务器参数
    host = "localhost"
    port = 8000
    server = HTTPServer((host, port), MyServer)
    
    print(f"Server started on http://{host}:{port}")
    
    try:
        # 启动服务器
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.server_close()
    print("Server stopped")