from django.shortcuts import render
from .models import Post
# imported from models.py

posts = [
# list of dictionry which
# is going to contain our posts
    {
        'authors': 'abc',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'authors': 'abc',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    }

]



def home(request):
    # This function will return
    # what user want to see in our homepage

    context = {
    # dictionary that contains
    # the list of dictionry

        'posts': Post.objects.all()
    }
    return render(request, 'E_Events/home.html', context)


def about(request):
    # This function will return
    # what user want to see in our about page

    return render(request, 'E_Events/about.html', {'title': 'About'})
