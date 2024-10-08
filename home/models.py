from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, null=True, blank=True)
    first_name = models.TextField(max_length=150, blank=True)
    last_name = models.TextField(max_length=150, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.TextField(max_length=150, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'