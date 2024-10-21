from django import forms
from ...models import Profile

class FamilyMemberForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'birth_date', 'gender', 'role']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }