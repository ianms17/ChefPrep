from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


# User profile model to save user input from form
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, default="", on_delete=models.CASCADE)

    # custom
    weight = models.IntegerField(null=True)
    feet = models.IntegerField(null=True)
    inches = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    goal = models.CharField(max_length=256, null=True)
    location = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=10, null=True)
    colorblind = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     profile = UserProfile(instance.pk)
#     profile.save()

