from django import forms
from ...models import Profile

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]

class UserOnboardingForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'birth_date', 'gender', 'role']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(choices=GENDER_CHOICES, attrs={'class': 'form-control'}),  # Gender dropdown
            'role': forms.Select(attrs={'class': 'form-control'}),
        }

    # Health fields
    condition = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Condition'}),
        required=False
    )
    doctor = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doctor Name'}),
        required=False
    )
    health_description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Health Description', 'rows': 3}),
        required=False
    )
    date_recorded = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=False
    )

    # Education fields
    school = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'School'}),
        required=False
    )
    class_record = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Class Name'}),
        required=False
    )
    teacher = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teacher Name'}),
        required=False
    )
    grade = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Grade'}),
        required=False
    )
    date_started = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))  # Add this


    # Event fields
    event_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
        required=False
    )
    event_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=False
    )
    event_description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Event Description', 'rows': 3}),
        required=False
    )

    # Finance fields
    transaction = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Transaction'}),
        required=False
    )
    amount = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
        required=False
    )
    finance_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=False
    )
    finance_description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Finance Description', 'rows': 3}),
        required=False
    )
