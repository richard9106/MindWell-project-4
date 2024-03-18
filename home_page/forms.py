"""Import form and models """
from django import forms
from .models import ContactForm


class UserContacForm(forms.ModelForm):
    """Contact form"""

    class Meta:
        """select the model"""
        model = ContactForm
        fields = ('name', 'email', 'consultation_type', 'message')
        labels = {
                'name': 'Name',
                'email': 'Email',
                'consultation_type': 'Choose a subject',
                'message': 'How can we help?'
            }
           
