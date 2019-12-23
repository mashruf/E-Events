from django.db.models.signals import post_save
# we want to get a post_save signal
# when a user is created

from django.contrib.auth.models import User

from django.dispatch import receiver
# is going to get some signals
# and perform task

from .models import Profile
# since we are creating Profile
# in our funtion



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
# creates user Profile

    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
# save created Profile

    instance.profile.save()
