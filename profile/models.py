""" models to manage info user"""
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# User profile.
class Profile(models.Model):
    """model user information"""
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile',
                                )
    first_name = models.CharField(max_length=254, default="Mi Name")
    last_name = models.CharField(max_length=254, default="Mi Last Name")
    image = models.ImageField(
        default='static/images/profile_images/user1.jpg',
        upload_to='static/images/profile_images/',
        )
    location = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        )
    email = models.EmailField(max_length=254)
    profession = models.CharField(max_length=254)
    description = models.TextField()
    create_on = models.DateTimeField(
        auto_now_add=True,
        )
    completed_info = models.BooleanField(default=False)

    class Meta:
        """meta class"""
        ordering = ['-id']

    def __str__(self):
        return f"{self.user} | location: {self.location}"


# create user afert some one create an account
# @receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """create the user"""
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)

