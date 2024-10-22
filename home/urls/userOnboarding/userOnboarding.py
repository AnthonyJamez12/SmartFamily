from django.urls import path
from ...views.userOnboarding.userOnboarding import user_onboarding

urlpatterns = [
    path('user_onboarding/', user_onboarding, name='user_onboarding'),     # url, to view function, to the name of url

]