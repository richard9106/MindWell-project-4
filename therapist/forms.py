"""Import form and models """
from django import forms
from .models import AppointmentManager


class UserAppointmentManager(forms.ModelForm):
    """Contact form"""

    class Meta:
        """select the model"""
        model = AppointmentManager
        fields = ('client', 'date', 'message')
       