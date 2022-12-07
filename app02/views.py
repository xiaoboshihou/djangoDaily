from django.shortcuts import render, reverse, HttpResponse

# Create your views here.


def index(request):
    url = reverse('app02:index_page')
    return HttpResponse('app02反向解析结果为%s' % url)
# def index(request):
#     return HttpResponse('我是app02的index page')

