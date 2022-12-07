import time

from wsgiref.simple_server import make_server
from jinja2 import Template


def index(environ):
    with open('index.html', 'r', encoding='utf-8') as f:
        response = f.read()
    return response.encode('utf-8')


def timer(environ):
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    with open('timer.html', 'r', encoding='utf-8') as f:
        data = f.read()
        template = Template(data)
    response = template.render({'xxx': now, 'user': 'lxy', 'role': 'xiaoboshihou'})  # 字符串替换
    return response.encode('utf-8')


url_patterns = [
    ('/index', index),
    ('/timer', timer)
]


def app(environ, start_response):  # 代表application
    start_response('200 OK', [('Content-Type', 'text/html')])

    # 拿到请求的url根据映射关系执行相应函数
    request_url = environ.get('PATH_INFO')
    for url in url_patterns:
        if url[0] == request_url:
            data = url[1](environ)
            break
        else:
            data = b'404'
    return [data]


if __name__ == '__main__':
    s = make_server('', 5000, app)
    print('监听5000')
    s.serve_forever()

