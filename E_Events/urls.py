# urls.py module will map the URLs
# that we want correspond to each
#view function

from django.urls import path
# this module is imported
# to run the the destinated path

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView
)


from . import views
# this module is imported
# to use the functions
# from the views.py module


urlpatterns = [
    path('', PostListView.as_view(), name='events-home'),
    # set the path empty to take us to homepage
    # set the name of the path events-home

    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    # will provide id of the route
    # and post detail

    path('post/new/', PostCreateView.as_view(), name='post-create'),
    # will share a template with post update

    path('about/', views.about, name='events-about'),
    # set the path /about to take us to about page
    # we are calling the funtion about
    # from views.py by view.about
    # set the name of the path events-about
]
