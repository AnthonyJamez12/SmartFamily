from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ...models import Profile

class FamilyMemberForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    gender = forms.ChoiceField(choices=Profile.GENDER_CHOICES, required=True)
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'birth_date', 'gender', 'role']