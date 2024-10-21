from django.urls import path
from ...views.home.home import *

urlpatterns = [
    path('home/', home_view, name='home'),

]