""" view from home page"""
from django.shortcuts import render
# from allauth.account.forms import LoginForm


# Create your views here.
def index(request):
    """Home page View"""
    return render(request, 'index.html')

