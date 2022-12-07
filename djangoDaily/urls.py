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
from django.contrib import admin
from django.urls import path, re_path, include, register_converter
from django.views.defaults import bad_request, permission_denied, page_not_found, server_error
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView

from app01.path_converters import MonthConverter
from app01.views import *
from myapp.views import MyView, GreetingView, MorningGreetingView

register_converter(MonthConverter, 'mon')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomePageView.as_view()),
    path('books/', BookListView.as_view()),
    path('about1/', GreetingView.as_view()),
    path('about/', MorningGreetingView.as_view()),
    re_path(r'^test/', test),
    path('test/400', error_test_400),
    path('test/403', error_test_403),
    path('test/404', error_test_404),
    path('test/500', error_test_500),
    path('login/', LoginView.as_view()),
    # re_path(r'^login/$', login, name='login_page'),
    re_path('^$', index),
    re_path(r'^index/$', index),
    # re_path('^login/$', login),
    # re_path(r'^index/$', index, name='index_page'),
    re_path(r'^article/$', index, name='index_page'),
    path('articles/<int:year>/<mon:month>/<slug:other>/', article_detail, name='aaa'),
    re_path(r'^app01/', include(('app01.urls', 'app01'))),
    re_path(r'^app02/', include(('app02.urls', 'app02'))),
]

handler400 = 'app01.views.my_custom_bad_request_view'
handler403 = 'app01.views.my_custom_permission_denied_view'
handler404 = 'app01.views.my_custom_page_not_found_view'
handler500 = 'app01.views.my_custom_error_view'

