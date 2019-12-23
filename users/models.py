from django.db import models

from django.contrib.auth.models import User
# we are extending the user model
# that django provides us

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # creating one to one relation with existing user models

    image = models.ImageField(default='default.jpg',upload_to='profile_pics')


    def __str__(self):
    # how we want to show the user and profile

        return f'{self.user.username} Profile'
