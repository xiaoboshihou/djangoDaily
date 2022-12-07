"""djangoDaily URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path

from app01 import views


urlpatterns = [
    re_path(r'^index/$', views.index, name='index_page'),
    re_path(r'^timer/$', views.timer),
    re_path(r'^home/$', views.home),
    re_path(r'^user/([a-zA-Z]+)/$', views.article, kwargs={'tag': 1}),
    re_path(r'^user/(\d{4})/$', views.article, kwargs={'tag': 2}),
    re_path(r'^user/(\d{2})/$', views.article, kwargs={'tag': 3}),
    # re_path(r'^article/$', views.article),
    # re_path(r'^article/(?P<article_id>\d+)/$', views.article),
    # re_path(r'^article/(\d+)/$', views.article),
    # path('/index', views.index),
    # path('/timer', views.timer),
    # path('/home', views.home),
]

