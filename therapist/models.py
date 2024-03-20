"""models to control therapist information"""

from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.
class Therapists(models.Model):
    """Info about Therapists"""
    first_name = models.CharField(max_length=255, primary_key=True)
    last_name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=200)
    bio = models.TextField()
    experience_years = models.PositiveIntegerField()
    location = models.CharField(max_length=200,  blank=True)
    profile_image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = price = models.DecimalField(max_digits=8, decimal_places=2,
                                        default=0.00)
    approved = models.BooleanField(default=False)

    class Meta:
        """ order by name"""
        ordering = ["first_name"]

    def __str__(self):
        """ Show the name in the list of therapisd admin"""
        return f"{self.first_name} {self.last_name}"


# Create your models here.
class AppointmentManager(models.Model):
    """Model for link user and their appointments"""
    client = models.ForeignKey(User,
                               on_delete=models.CASCADE, 
                               related_name='userprofile')
    
    date = models.DateTimeField(null=True,
                                blank=True,
                                )
    message = models.TextField()

    class Meta:
        """ order by name"""
        ordering = ["date"]

    def __str__(self):
        """ Show the name in the list of therapisd admin"""
        return f"{self.client} have an appointmet in :{self.date} "
