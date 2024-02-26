from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """ view for index.html"""
    return HttpResponse('index.html')
