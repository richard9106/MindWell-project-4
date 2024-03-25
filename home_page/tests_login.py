from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings


class TestLoginViews(TestCase):
    """Test inf the user can login"""   

    def setUp(self):
        self.user = User.objects.create_user(
            username='myusername',
            password='myPassword',
            email='test@test.com'
        )
        self.user.save()
        
    def test_login_page_login_without_verification(self):
        """testing Login user """
        response = self.client.post(reverse('account_login'),
                                    {'login': 'myusername',
                                    'password': 'myPassword'})
        self.assertTrue(response, settings.LOGIN_REDIRECT_URL)
