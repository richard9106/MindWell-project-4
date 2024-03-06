from django.shortcuts import render
from .forms import WorkWithUsForm


# Create your views here.
def work_with_us(request):
    """ work with us form view"""
    work_with_us_form = WorkWithUsForm(request.POST)

    return render(
        request,
        'workwithus.html',
        {"work_with_us_form": work_with_us_form})
