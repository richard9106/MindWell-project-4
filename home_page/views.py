""" view from home page"""
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
# from allauth.account.forms import LoginForm


# Create your views here.
def index(request):
    """Home page View"""
    
    if request.method == 'POST':
        lform = AuthenticationForm(request=request, data = request.POST)
        sform = UserCreationForm(request.POST)
        if lform.is_valid():
            username = lform.cleaned_data['username']
            password = lform.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('userpage')
        elif sform.is_valid():
            sform.save()
            return HttpResponseRedirect('userpage')

         
    else:
        lform = AuthenticationForm()
        sform = UserCreationForm()
        return render(request, 'index.html', {
            'login_form': lform, 'singup_form': sform})

