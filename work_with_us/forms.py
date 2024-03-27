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
            'email',
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
            'email': 'Email',
            'profile_image': 'Profile Image',
            'experience_years': 'Experience Years',
            'price': 'Your Price',
            'bio': 'About Me',
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['profile_image'].options = {
                'tags': 'new_image',
                'format': 'png',
                'crop': 'limit', 'width': 1000, 'height': 1000,
                'eager': [{'crop': 'fill', 'width': 200, 'height': 200}]
            }
