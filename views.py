from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Hello world')

def check(request):
    return HttpResponse('Hi this is a change made to git using clone method!')