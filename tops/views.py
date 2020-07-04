from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


# Create your views here.


class HelloView(View):

    def get(self, request):
        return HttpResponse('<h1>hello, world</h1>')
