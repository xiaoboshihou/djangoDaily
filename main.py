from wsgiref.simple_server import make_server
from djangoDaily.urls import url_patterns


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

