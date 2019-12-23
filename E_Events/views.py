from django.shortcuts import render

from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)

from .models import Post



def home(request):
    # This function will return
    # what user want to see in our homepage

    context = {
    # dictionary that contains
    # the list of dictionry

        'posts': Post.objects.all()
    }
    return render(request, 'E_Events/home.html', context)

class PostListView(ListView):
    # will provide list view

    model = Post
    # this model will tell our ListView
    # what model to query

    template_name = 'E_Events/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts' # setting home template as default
    ordering = ['-date_posted'] # will show our post newest to oldest

class PostDetailView(DetailView):
# will provide details of post

    model = Post


class PostCreateView(CreateView):
# will create new post

    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
    # will override the form valid method

        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    # This function will return
    # what user want to see in our about page

    return render(request, 'E_Events/about.html', {'title': 'About'})
