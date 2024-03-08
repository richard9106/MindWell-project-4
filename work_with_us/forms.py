""" used the same model to display therapis from therapist app"""
from django import forms
from therapist.models import Therapists


class WorkWithUsForm(forms.ModelForm):
    """ Create the model for collaborateForm"""
    
    class Meta:
        """We select the files to apear in the form"""
        model = Therapists
        fields = (
            'first_name',
            'last_name',
            'specialization',
            'experience_years',
            'location',
            'profile_image',
            'price',
            'bio',
            )
        labels = {
            'first_name': 'First Name',
            'last_name': 'Lasst Name',
            'profile_image': 'Profile Image',
            'experience_years': 'Experience Years',
            'price': 'Your Price',
            'bio': 'About Me',
        }

