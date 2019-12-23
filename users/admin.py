from django.contrib import admin

from .models import Profile
# importing from models.py of users

admin.site.register(Profile) # registering the profile
