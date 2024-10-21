from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ...forms.userOnboarding.userOnboarding import UserOnboardingForm
from ...models import *

@login_required
def user_onboarding(request):
    print("Executing user_onboarding view")
    profile = request.user.profile
    print(f"Logged in user: {request.user.username}, Profile ID: {profile.id}")

    if request.method == 'POST':
        print("Processing POST request")
        
        # Create the form instance with the POST data
        form = UserOnboardingForm(request.POST, instance=profile)

        if form.is_valid():
            print("Profile form is valid, saving main profile")
            # Save the main Profile form data
            profile = form.save()

            # 1. Save Health Records
            conditions = request.POST.getlist('condition')
            doctors = request.POST.getlist('doctor')
            descriptions = request.POST.getlist('health_description')
            dates = request.POST.getlist('date_recorded')

            print("Health Records:", conditions, doctors, descriptions, dates)
            # Clear previous Health Records and create new ones
            HealthRecord.objects.filter(profile=profile).delete()
            for condition, doctor_name, description, date in zip(conditions, doctors, descriptions, dates):
                if condition or doctor_name:  # Save only if at least one field is filled
                    doctor_instance, _ = Doctor.objects.get_or_create(name=doctor_name.strip())
                    HealthRecord.objects.create(
                        profile=profile,
                        condition=condition or "",
                        doctor=doctor_instance,
                        description=description or "",
                        date_recorded=date,
                    )

            # 2. Save Education Records
            schools = request.POST.getlist('school')
            class_names = request.POST.getlist('class_record')
            teacher_names = request.POST.getlist('teacher')
            grades = request.POST.getlist('grade')
            start_dates = request.POST.getlist('date_started')

            print("Education Records - Schools:", schools)
            print("Education Records - Classes:", class_names)
            print("Education Records - Teachers:", teacher_names)
            print("Education Records - Grades:", grades)

            # Clear previous Education Records and create new ones
            EducationRecord.objects.filter(profile=profile).delete()
            for school, class_name, teacher_name, grade, date_started in zip(schools, class_names, teacher_names, grades, start_dates):
                if school or class_name or teacher_name:
                    teacher_instance, _ = Teacher.objects.get_or_create(name=teacher_name.strip())
                    class_instance, _ = Class.objects.get_or_create(class_name=class_name.strip(), teacher=teacher_instance, defaults={'grade': grade})
                    EducationRecord.objects.create(
                        profile=profile,
                        school=school or "",
                        class_record=class_instance,
                        date_started=date_started,  # Save the date_started value
                    )
            # 3. Save Event Records
            event_names = request.POST.getlist('event_name')
            event_dates = request.POST.getlist('event_date')
            event_descriptions = request.POST.getlist('event_description')

            print("Event Records - Names:", event_names)
            print("Event Records - Dates:", event_dates)
            print("Event Records - Descriptions:", event_descriptions)

            # Clear previous Event Records and create new ones
            Event.objects.filter(profile=profile).delete()
            for name, date, description in zip(event_names, event_dates, event_descriptions):
                if name:  # Save only if at least one field is filled
                    Event.objects.create(
                        profile=profile,
                        event_name=name or "",
                        event_date=date,
                        event_description=description or "",
                    )

            # 4. Save Finance Records
            transactions = request.POST.getlist('transaction')
            amounts = request.POST.getlist('amount')
            finance_dates = request.POST.getlist('finance_date')
            finance_descriptions = request.POST.getlist('finance_description')

            print("Finance Records - Transactions:", transactions)
            print("Finance Records - Amounts:", amounts)
            print("Finance Records - Dates:", finance_dates)
            print("Finance Records - Descriptions:", finance_descriptions)

            # Clear previous Finance Records and create new ones
            FinanceRecord.objects.filter(profile=profile).delete()
            for transaction, amount, date, description in zip(transactions, amounts, finance_dates, finance_descriptions):
                if transaction:  # Save only if at least one field is filled
                    FinanceRecord.objects.create(
                        profile=profile,
                        transaction=transaction or "",
                        amount=amount or 0,
                        date=date,
                        description=description or "",
                    )

            # Show success message
            messages.success(request, 'Profile updated successfully!')
            print("Profile updated successfully")

            # Redirect to the home page
            return redirect('home')
        else:
            print("Profile form is not valid")
            print(form.errors)  # Print form errors to see why it's invalid

    else:
        print("Processing GET request")
        # Create a new form with the user's profile
        form = UserOnboardingForm(instance=profile)

    return render(request, 'userOnboarding/user_onboarding.html', {'form': form})
