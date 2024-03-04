""" models to manage info user"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# User profile.
class Profile(models.Model):
    """model user information"""
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile',
                                verbose_name='User')
    image = models.ImageField(
        default='statics/images/profile_images/default.jpeg',
        upload_to='statics/images/profile_images/',
        verbose_name='profile_image')
    location = models.CharField(
        max_length=250, 
        null=True, 
        blank=True)
    email = models.EmailField(max_length=254)
    profession = models.CharField(max_length=254)
    description = models.TextField()
    create_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name='creation_date')

    class Meta:
        """meta class"""
        verbose_name = 'profile'
        verbose_name = 'creation_date'
        ordering = ['-id']

    def __str__(self):
        return self.user.username
    

def create_user_profile(sender,instance, created, **kwargs):
    """define the function to create the profile""" 
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender,instance, created, **kwargs):
    """define the function to save the profile""" 
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
