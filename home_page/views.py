""" view from home page"""
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserContacForm


# Create your views here.
def index(request):
    """Home page View"""
    return render(request, 'index.html')


def contact(request):
    """contact page view"""

    if request.method == 'POST':
        form_contact = UserContacForm(data=request.POST)
        if form_contact.is_valid():
            form_contact.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your message was send successfully')
            return redirect('contact')
        else:
            messages.add_message(
                request,
                messages.WARNING,
                "Something has gone wrong try later")

    return render(request, 'contact.html', {'form': UserContacForm})
