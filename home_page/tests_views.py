from django.test import TestCase
from . import views


# Create your tests here.
class TestCalls(TestCase):
    """call the views and see if the page load"""
    def test_call_view_home_page(self):
        """call the home page from anonumous user"""
        response = self.client.get(views.index, follow=True)
        self.assertTrue(response, 'home/')

    def test_call_view_contact_page(self):
        """call the home page from anonumous user"""
        response = self.client.get(views.contact, follow=True)
        self.assertTrue(response, 'contact/')
