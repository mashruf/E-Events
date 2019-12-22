from django import forms
# importing form from django

from django.contrib.auth.models import User
# importing user models

from django.contrib.auth.forms import UserCreationForm
# importing user creation form


class UserRegisterForm(UserCreationForm):
# will inherit the UserCreationForm

    email = forms.EmailField() # additional email field on the form

    class Meta:
    # within meta we specified
    # the model that we want
    # this form to interact with

        model = User # whenever this form validates
                     # it will create new user

        fields = ['username', 'email', 'password1', 'password2'] # this fields are going
                                                                 # to be shown on our form