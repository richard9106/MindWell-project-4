"""models to control therapist information"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Therapists(models.Model):
    """Info about Therapists"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=200)
    bio = models.TextField(max_length=1000, blank=True)
    experience_years = models.PositiveIntegerField()
    location = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='static/images/therapist_profile_pics/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)



    # def __str__(self):
    #     """"""
    #     return self.user