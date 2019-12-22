from django.shortcuts import render, redirect
from django.contrib import messages
# imported to show flash message
# that we have recieved valid data

from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm


def register(request):
# This function will return
# what user want to see in our registration homepage

        if request.method == 'POST':
        # if we get a POST request
        # we will validate the data

            form = UserRegisterForm(request.POST)
            if form.is_valid():
            # if the data are valid

                form.save() # save data to db
                username = form.cleaned_data.get('username') # get username from the form
                messages.success(request, f'Account created for {username}!') # success message
                return redirect('login') # takes user to login page
        else:
        # if we get a GET request
        # it will return a empty form

            form = UserRegisterForm() # leave the form empty

        return render(request, 'users/register.html', {'form':form},)

@login_required
def profile(request):
# to view user's profile
    return render(request, 'users/profile.html')
