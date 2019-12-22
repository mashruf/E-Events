from django.db import models
from django.utils import timezone
# imported for time facilities

from django.contrib.auth.models import User
# imported for delet facilities

class Post(models.Model):
    # its a class that inherits from
    # the models class
    # each class going to create
    # own field on database

    title = models.CharField(max_length=100) # title of the post
    content = models.TextField() # content of the post
    date_posted = models.DateTimeField(default=timezone.now) #date of the post
    author = models.ForeignKey(User, on_delete=models.CASCADE) #author of the post

    def __str__(self):
    # this method is for
    # how we want to print
    # our post
        return self.title
