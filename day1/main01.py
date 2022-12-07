# S端 server application
import socket
import time

from jinja2 import Template


def make_server(ip, port, app):  # 代表server
    # 处理套接字通信相关事宜
    sock = socket.socket()
    sock.bind((ip, port))
    sock.listen(1)
    print('Starting development server at http://%s:%s/' % (ip, port))
    while True:
        conn, addr = sock.accept()

        # 1、接收浏览器发来的请求信息
        recv_data = conn.recv(1024)
        # print(recv_data.decode('utf-8'))

        # 1.2 对http协议的消息加以处理，简单示范如下
        ll = recv_data.decode('utf-8').split('\r\n')
        head_ll = ll[0].split(' ')
        environ = {'PATH_INFO': head_ll[1], 'method': head_ll[0]}

        # 2：将请求信息处理结果environ交给application，这样application便无需再关注请求信息的处理，可以更加专注于业务逻辑的处理
        res = app(environ)

        # 3：按照http协议向浏览器返回消息
        # 3.1 返回响应首行
        conn.send(b'HTTP/1.1 200 OK\r\n')
        # 3.2 返回响应头（可省略）
        conn.send(b'Content-Type: text/html\r\n\r\n')
        # 3.3 返回响应体
        conn.send(res)

        conn.close()


def app(environ):  # 代表application
    # 处理业务逻辑
    # response = 'Hello World'

    # 返回给浏览器数据(符合html格式)
    # response = '<h1>hello web</h1><img src="https://www.baidu.com/img/bd_logo1.png"></img>'

    # 返回html页面
    # with open('index.html', 'r', encoding='utf-8') as f:
    #     response = f.read()

    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    # 返回html页面
    with open('timer.html', 'r', encoding='utf-8') as f:
        data = f.read()
        template = Template(data)
    # response = data.replace('{{ xxx }}', now)  # 字符串替换
    response = template.render({'xxx': now, 'user': 'lxy', 'role': 'xiaoboshihou'})  # 字符串替换

    return response.encode('utf-8')


if __name__ == '__main__':
    make_server('127.0.0.1', 5000, app)

