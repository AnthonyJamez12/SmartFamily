from django.db import models
from django.contrib.auth.models import User


class Family(models.Model):
    family_name = models.CharField(max_length=255)  # Field to identify the family
    
    def __str__(self):
        return self.family_name


class Profile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    ROLE_CHOICES = [
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('child', 'Child'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.TextField(max_length=150, blank=True)
    last_name = models.TextField(max_length=150, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='child') 
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='members', null=True, blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'



class Doctor(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)  # Doctor's location (e.g., hospital, clinic)
    specialty = models.CharField(max_length=255, blank=True)  # Optional: Doctor's specialty

    def __str__(self):
        return self.name


class HealthRecord(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    condition = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)  # Link to Doctor
    date_recorded = models.DateField()

    def __str__(self):
        return f'{self.condition} for {self.profile.user.username}'


# Teacher model for linking to class and education records
class Teacher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)  # Optional: Teacher's contact info

    def __str__(self):
        return self.name


class Class(models.Model):
    class_name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)  # Link to Teacher
    grade = models.CharField(max_length=50)  # Class grade (e.g., A, B, Pass, Fail)

    def __str__(self):
        return f'{self.class_name} taught by {self.teacher.name if self.teacher else "Unknown"}'


class EducationRecord(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
    class_record = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)  # Link to Class
    description = models.TextField(blank=True)
    date_started = models.DateField()

    def __str__(self):
        return f'{self.class_record.class_name if self.class_record else "No Class"} for {self.profile.user.username}'


class Event(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=255)
    event_date = models.DateField()
    event_description = models.TextField(blank=True)

    def __str__(self):
        return f'Event: {self.event_name} for {self.profile.user.username}'


class FinanceRecord(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    transaction = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.transaction} for {self.profile.user.username}'
