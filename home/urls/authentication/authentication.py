from django.urls import path
from ...views.authentication.authentication import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', register_view, name='register'),
]