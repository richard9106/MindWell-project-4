from django.shortcuts import render, redirect
from .forms import WorkWithUsForm
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def work_with_us(request):
    """ work with us form view"""
    if request.method == 'POST':
        work_with_us_form = WorkWithUsForm(request.POST)
        if work_with_us_form.is_valid():
            work_with_us_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Profile received! I endeavour to respond within 2 working days.")
        else:
            messages.add_message(
                request,
                messages.WARNING,
                "Something has gone wrong check your info")

    return render(
        request,
        'workwithus.html',
        {"work_with_us_form": WorkWithUsForm})
