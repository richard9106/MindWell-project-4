from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def appointments(request):
    """Appointment main view"""
    return render(request, 'appointments.html')
