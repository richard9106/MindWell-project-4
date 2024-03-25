from django.test import TestCase
from .forms import UserProfileForm


# Create your tests here.
class TestUserProfileForm(TestCase):
    """testing user eddit info or add info is valid"""
    def test_form_is_valid(self):
        """pased infp to the form and see if valid"""
        user_profile_form = UserProfileForm({
            'first_name': 'Juana',
            'last_name': 'Lopez',
            'location': 'Madrid',
            'email': 'jauna@correo.com',
            'profession': 'Chef',
            'description': 'hi I am juana'
        })
        self.assertTrue(user_profile_form.is_valid())

    def test_form_is_not_valid(self):
        """pased infp to the form and see if valid"""
        user_profile_form = UserProfileForm({
            'first_name': '',
            'last_name': '',
            'location': '',
            'email': '',
            'profession': '',
            'description': ''
        })
        self.assertFalse(user_profile_form.is_valid())