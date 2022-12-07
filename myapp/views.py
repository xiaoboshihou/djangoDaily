from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
class MyView(View):
    def get(self, request):
        return HttpResponse('GET result')

    def post(self, request):
        return HttpResponse('POST result')


class GreetingView(View):
    greeting = 'Good Day'

    def get(self, request):
        return HttpResponse(self.greeting)


class MorningGreetingView(GreetingView):
    greeting = 'Morning to ya'

