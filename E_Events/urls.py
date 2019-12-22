# urls.py module will map the URLs
# that we want correspond to each
#view function


from django.urls import path
# this module is imported
# to run the the destinated path

from . import views
# this module is imported
# to use the functions
# from the views.py module


urlpatterns = [
    path('', views.home, name='events-home'),
    # set the path empty to take us to homepage
    # we are calling the funtion home
    # from views.py by view.home
    # set the name of the path events-home

    path('about/', views.about, name='events-about'),
    # set the path /about to take us to about page
    # we are calling the funtion about
    # from views.py by view.about
    # set the name of the path events-about
]
