from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ...forms.home.home import FamilyMemberForm
from ...forms.userOnboarding.userOnboarding import UserOnboardingForm
from ...models import *
from django.contrib.auth.models import User
import uuid
from django.core.serializers.json import DjangoJSONEncoder
import json

@login_required
def home_view(request):
    profile = request.user.profile

    # Check if the user has a family association; if not, create one
    if not profile.family:
        family = Family.objects.create(family_name=f"{profile.first_name}'s Family", family_id=uuid.uuid4())
        profile.family = family
        profile.save()

    family_members = Profile.objects.filter(family=profile.family) if profile.family else []
    family_member_form = FamilyMemberForm()  # Ensure form is defined and passed to the context

    health_records = HealthRecord.objects.filter(profile=profile)
    education_records = EducationRecord.objects.filter(profile=profile)
    events = Event.objects.filter(profile=profile)
    finance_records = FinanceRecord.objects.filter(profile=profile)
    doctors = Doctor.objects.filter(healthrecord__profile=profile).distinct()
    finance_records = FinanceRecord.objects.filter(profile=profile)

    finance_labels = [record.transaction for record in finance_records]
    finance_amounts = [float(record.amount) for record in finance_records]
    # Initialize forms
    onboarding_form = UserOnboardingForm(instance=profile)
    if request.method == 'POST':
        if 'add_family_member' in request.POST:
            family_member_form = FamilyMemberForm(request.POST)
            if family_member_form.is_valid():
                # Create the user
                user = family_member_form.save()

                # Create the profile and set the family relationship
                Profile.objects.create(
                    user=user,
                    first_name=family_member_form.cleaned_data['first_name'],
                    last_name=family_member_form.cleaned_data['last_name'],
                    birth_date=family_member_form.cleaned_data['birth_date'],
                    gender=family_member_form.cleaned_data['gender'],
                    role=family_member_form.cleaned_data['role'],
                    family=profile.family  # Associate with the current user's family
                )

                messages.success(request, f"Family member '{user.username}' added successfully!")
                return redirect('home')
            else:
                messages.error(request, "Error adding family member. Please check the form.")

        elif 'onboarding_submit' in request.POST:
            onboarding_form = UserOnboardingForm(request.POST, instance=profile)
            if onboarding_form.is_valid():
                profile = onboarding_form.save()

                # Process Health Records
                HealthRecord.objects.filter(profile=profile).delete()
                conditions = request.POST.getlist('condition')
                doctors = request.POST.getlist('doctor')
                descriptions = request.POST.getlist('health_description')
                dates = request.POST.getlist('date_recorded')

                for condition, doctor_name, description, date in zip(conditions, doctors, descriptions, dates):
                    if condition or doctor_name:
                        doctor_instance, created = Doctor.objects.get_or_create(name=doctor_name.strip())
                        HealthRecord.objects.create(
                            profile=profile,
                            condition=condition or "",
                            doctor=doctor_instance,
                            description=description or "",
                            date_recorded=date,
                        )

                # Process Education Records
                EducationRecord.objects.filter(profile=profile).delete()
                schools = request.POST.getlist('school')
                class_names = request.POST.getlist('class_record')
                teacher_names = request.POST.getlist('teacher')
                grades = request.POST.getlist('grade')
                start_dates = request.POST.getlist('date_started')

                for school, class_name, teacher_name, grade, date_started in zip(schools, class_names, teacher_names, grades, start_dates):
                    if school or class_name or teacher_name:
                        teacher_instance, _ = Teacher.objects.get_or_create(name=teacher_name.strip())
                        class_instance, _ = Class.objects.get_or_create(class_name=class_name.strip(), teacher=teacher_instance, defaults={'grade': grade})
                        EducationRecord.objects.create(
                            profile=profile,
                            school=school or "",
                            class_record=class_instance,
                            date_started=date_started,
                        )

                # Process Event Records
                Event.objects.filter(profile=profile).delete()
                event_names = request.POST.getlist('event_name')
                event_dates = request.POST.getlist('event_date')
                event_descriptions = request.POST.getlist('event_description')

                for name, date, description in zip(event_names, event_dates, event_descriptions):
                    if name:
                        Event.objects.create(
                            profile=profile,
                            event_name=name or "",
                            event_date=date,
                            event_description=description or "",
                        )

                # Process Finance Records
                FinanceRecord.objects.filter(profile=profile).delete()
                transactions = request.POST.getlist('transaction')
                amounts = request.POST.getlist('amount')
                finance_dates = request.POST.getlist('finance_date')
                finance_descriptions = request.POST.getlist('finance_description')

                for transaction, amount, date, description in zip(transactions, amounts, finance_dates, finance_descriptions):
                    if transaction:
                        FinanceRecord.objects.create(
                            profile=profile,
                            transaction=transaction or "",
                            amount=amount or 0,
                            date=date,
                            description=description or "",
                        )

                messages.success(request, 'Profile updated successfully!')
                return redirect('home')
            else:
                print("Profile form is not valid:", onboarding_form.errors)

    context = {
        'profile': profile,
        'family_members': family_members,
        'health_records': health_records,
        'education_records': education_records,
        'events': events,
        'finance_records': finance_records,
        'doctors': doctors,
        'family_member_form': family_member_form,
        'onboarding_form': onboarding_form,
        'finance_labels': json.dumps(finance_labels, cls=DjangoJSONEncoder),
        'finance_amounts': json.dumps(finance_amounts, cls=DjangoJSONEncoder),
    }

    return render(request, 'home/home.html', context)

