"""models to control therapist information"""

from django.db import models
# from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



# Create your models here.
class Therapists(models.Model):
    """Info about Therapists"""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=200)
    bio = models.TextField(max_length=1000, blank=True)
    experience_years = models.PositiveIntegerField()
    location = models.CharField(max_length=200,  blank=True)
    profile_picture = CloudinaryField('image', default='placeholder')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    approved = models.BooleanField(default=False)

    class Meta:
        """ order by name"""
        ordering = ["first_name"]

    def __str__(self):
        """ Show the name in the list of therapisd admin"""
        return f"{self.first_name} {self.last_name}"
