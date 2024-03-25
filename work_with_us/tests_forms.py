"""testing work with us form to get info  therapist"""
from django.test import TestCase
from .forms import WorkWithUsForm


# Create your tests here.
class TestWorkWithUsForm(TestCase):
    """testing user eddit info or add info"""
    def test_form_is_valid(self):
        """pased info to the form and see if valid"""
        work_with_us_form = WorkWithUsForm({
            'first_name': 'Leslie',
            'last_name': 'Perez',
            'email': 'leslie@correo.com',
            'experience_years': '5',
            'location': 'Houston',
            'specialization': 'Psychologist',
            'price': '250',
            'bio': 'hi this is Leslie',
        })
        self.assertTrue(work_with_us_form.is_valid())

    def test_form_is_not_valid(self):
        """pased empty fields and see if the form is not valid"""
        work_with_us_form = WorkWithUsForm({
            'first_name': '',
            'last_name': '',
            'email': '',
            'experience_years': '',
            'location': '',
            'specialization': '',
            'price': '',
            'bio': 'hi this is Leslie',
        })
        self.assertFalse(work_with_us_form.is_valid())

    def test_first_name_is_required(self):
        """Test if firs_name field is empty"""
        work_with_us_form = WorkWithUsForm({
            'first_name': '',
            'last_name': 'Perez',
            'email': 'leslie@correo.com',
            'experience_years': '5',
            'location': 'Houston',
            'specialization': 'Psychologist',
            'price': '250',
            'bio': 'hi this is Leslie',
        })
        self.assertFalse(work_with_us_form.is_valid(),
                         msg="First Name was not provided, but the form is valid")
    
    def test_email_is_required(self):
        """Test if email field is empty"""
        work_with_us_form = WorkWithUsForm({
            'first_name': 'Leslei',
            'last_name': 'Perez',
            'email': '',
            'experience_years': '5',
            'location': 'Houston',
            'specialization': 'Psychologist',
            'price': '250',
            'bio': 'hi this is Leslie',
        })
        self.assertFalse(work_with_us_form.is_valid(),
                         msg="Email was not provided, but the form is valid")

    def test_bio_is_required(self):
        """Test if bio field is empty"""
        work_with_us_form = WorkWithUsForm({
            'first_name': 'Leslei',
            'last_name': 'Perez',
            'email': '',
            'experience_years': '5',
            'location': 'Houston',
            'specialization': 'Psychologist',
            'price': '250',
            'bio': '',
        })
        self.assertFalse(work_with_us_form.is_valid(),
                         msg="Bio was not provided, but the form is valid")
        
    def test_price_is_required(self):
        """Test if price field is empty"""
        work_with_us_form = WorkWithUsForm({
            'first_name': 'Leslei',
            'last_name': 'Perez',
            'email': '',
            'experience_years': '5',
            'location': 'Houston',
            'specialization': 'Psychologist',
            'price': '',
            'bio': 'this is my bio',
        })
        self.assertFalse(work_with_us_form.is_valid(),
                         msg="Price was not provided, but the form is valid")