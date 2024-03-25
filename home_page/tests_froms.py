"""testing work with us form to get info  therapist"""
from django.test import TestCase
from .forms import UserContacForm


# Create your tests here.
class TestContactForm(TestCase):
    """testing user eddit info or add info"""
    def test_contact_form_is_valid(self):
        """pased info to the form and see if valid"""
        contact_form = UserContacForm({
            'name': 'Carlos',
            'email': 'carlos@correo.com',
            'consultation_type': '1',
            'message': 'Hi thanks for you help',
        })
        self.assertTrue(contact_form.is_valid(), msg="contact form send")

    def test_name_is_required(self):
        """Test if firs_name field is empty"""
        contact_form = UserContacForm({
            'name': ' ',
            'email': 'carlos@correo.com',
            'consultation_type': '1',
            'message': 'Hi thanks for you help',
        })
        self.assertFalse(contact_form.is_valid(),
                         msg="Name was not provided, but the form is valid")

    def test_email_is_required(self):
        """Test if firs_name field is empty"""
        contact_form = UserContacForm({
            'name': 'carlos',
            'email': '',
            'consultation_type': '1',
            'message': 'Hi thanks for you help',
        })
        self.assertFalse(contact_form.is_valid(),
                         msg="Email was not provided, but the form is valid")

    def test_message_is_required(self):
        """Test if firs_name field is empty"""
        contact_form = UserContacForm({
            'name': ' Carlos',
            'email': 'carlos@correo.com',
            'consultation_type': '1',
            'message': '',
        })
        self.assertFalse(contact_form.is_valid(),
                         msg="Message was not provided, but the form is valid")

