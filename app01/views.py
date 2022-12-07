import time
import datetime

from django.shortcuts import HttpResponse, render, reverse, redirect
from django.core.exceptions import SuspiciousFileOperation, PermissionDenied
from django.http import Http404
from django.views.generic.base import TemplateView
from django.views import View
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from jinja2 import Template

from app01.models import Book


# Create your views here.
def timer(func):
    def wrapper(request, *args, **kwargs):
        start = time.time()
        ret = func(request, *args, **kwargs)
        print('函数执行的时间是{}'.format(time.time()-start))
        return ret
    return wrapper
# def timer(request):
#     now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
#     return render(request, 'timer.html', {'xxx': now, 'user': 'lxy', 'role': 'xiaoboshihou'})
# def timer(environ):
#     now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
#     with open('templates/timer.html', 'r', encoding='utf-8') as f:
#         data = f.read()
#         template = Template(data)
#     response = template.render({'xxx': now, 'user': 'lxy', 'role': 'xiaoboshihou'})  # 字符串替换
#     return response.encode('utf-8')


def deco1(func):
    def wrapper(request, *args, **kwargs):
        print('==>deco1')
        ret = func(request, *args, **kwargs)
        return ret
    return wrapper


def deco2(func):
    def wrapper(request, *args, **kwargs):
        print('==>deco2')
        ret = func(request, *args, **kwargs)
        return ret
    return wrapper


# 装饰列表
decorator = [timer, deco1, deco2]


# CBV视图
@method_decorator(decorator, name='get')
class LoginView(View):
    def dispatch(self, request, *args, **kwargs):
        obj = super().dispatch(request, *args, **kwargs)
        return obj

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'lxy' and password == '123':
            return HttpResponse('登录成功')
        else:
            return HttpResponse('账号或密码错误')


class BookListView(ListView):
    model = Book

    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest('publication_date')
        response = HttpResponse()

        response['Last-Modified'] = last_book.publication_date.strftime('%Y-%m-%d %X')
        return response

    def get(self, request):
        books = Book.objects.all()
        names = '|'.join([book.name for book in books])
        return HttpResponse(names)


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'eg'
        context['age'] = '18'
        context['title'] = 'dsb'

        return context


def error_test_400(request):
    raise SuspiciousFileOperation('抛出400异常')


def error_test_403(request):
    raise PermissionDenied('抛出403异常')


def error_test_404(request):
    raise Http404('抛出404异常')


def error_test_500(request):
    xxx


def my_custom_bad_request_view(request, exception):  # 400
    '''
    处理400异常的视图，必须接收两个参数

    参数request:
    参数exception: 捕获的异常值

    返回值: django规定该函数需要返回一个HttpResponseBadRequest类的对象
           可以查看该类的源码，该类是HttpResponse的子类，并设置status_code = 400
    '''
    print('====>400')
    response = render(request, '400.html', {'exception': exception})
    response.status_code = 400  # 如果不设置，默认状态码为200
    return response


def my_custom_permission_denied_view(request, exception):  # 403
    '''
    处理403异常的视图，必须接收两个参数

    参数request:
    参数exception: 捕获的异常值

    返回值: django规定该函数需要返回一个HttpResponseForbidden类的对象
           可以查看该类的源码，该类是HttpResponse的子类，并设置status_code = 403
    '''
    print('====>403')
    response = render(request, '403.html', {'exception': exception})
    response.status_code = 403  # 如果不设置，默认状态码为200
    return response


def my_custom_page_not_found_view(request, exception):  # 404
    '''
    处理404异常的视图，必须接收两个参数

    参数request:
    参数exception: 捕获的异常值

    返回值: django规定该函数需要返回一个HttpResponseNotFound类的对象
           可以查看该类的源码，该类是HttpResponse的子类，并设置status_code = 404
    '''
    print('====>404')
    response = render(request, '404.html', {'exception': exception})
    response.status_code = 404  # 如果不设置，默认状态码为200
    return response


def my_custom_error_view(request):  # 500
    '''
    处理500异常的视图，只接收一个参数

    返回值: django规定该函数需要返回一个HttpResponseServerError类的对象
           可以查看该类的源码，该类是HttpResponse的子类，并设置status_code = 500
    '''
    print('====>500')
    response = render(request, '500.html', )  # 服务端的错误本就不应该暴露给客户端
    response.status_code = 500  # 如果不设置，默认状态码为200
    return response


def article_detail(request, year, month, other):
    print(year, type(year))
    print(month, type(month))
    print(other, type(other))
    print(reverse('aaa', args=(1988, 12, 'hello')))
    return HttpResponse('xxxx')


def year_archive(request, year):
    print(year, type(year))
    return HttpResponse('year_archive page')


def detail_view(request, article_id):
    print(article_id, type(article_id))
    return HttpResponse('detail_view page')


def edit_view(request, article_id):
    print(article_id, type(article_id))
    return HttpResponse('edit_view page')


def delete_view(request, article_id):
    print(article_id, type(article_id))
    return HttpResponse('delete_view page')


def login(request):
    if request.method == 'GET':
        # 当为get请求时，返回login.html页面,页面中的{% url 'login_page' %}会被反向解析成路径：/login/
        return render(request, 'login.html')

    # 当为post请求时，可以从request.POST中取出请求体的数据
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    if name == 'lxy' and pwd == '123':
        current_user = name
        # url = reverse('index_page')  # reverse会将别名'index_page'反向解析成路径：/index/
        # return redirect(url)  # 重定向到/index/
        return render(request, 'index.html', locals())
    else:
        msg = '用户名或密码错误'
        return render(request, 'login.html', locals())


def index(request):
    return render(request, 'index.html')
# def index(request):
#     url = reverse('app01:index_page')
#     return HttpResponse('app01的反向解析结果为%s' % url)
# def index(request):
#     return render(request, 'index.html')
# def index(request):
#     now = datetime.datetime.now()
#     ctime = now.strftime('%Y-%m-%d %X')
#     return render(request, 'index.html', {'ctime': ctime})
# def index(environ):
#     with open('templates/index.html', 'r', encoding='utf-8') as f:
#         response = f.read()
#     return response.encode('utf-8')


def home(request):
    return render(request, 'home.html')
# def home(environ):
#     with open('templates/home.html', 'r', encoding='utf-8') as f:
#         response = f.read()
#     return response.encode('utf-8')


# 带形参,指定默认参数值
def article(request, x, tag):
    if tag == 1:
        print('name is %s' % x)
    elif tag == 2:
        print('year is %s' % x)
    elif tag == 3:
        print('mon is %s' % x)
    return HttpResponse('ok')
# def article(request, article_id='1'):
#     return HttpResponse('id为 %s 的文章内容...' % article_id)


def test(request):
    names = ['lxy1', 'lxy2']
    dic = {'name': 'lxy1', 'age': 18, 'sex': 'male'}
    list1 = []

    return render(request, 'test.html', locals())

