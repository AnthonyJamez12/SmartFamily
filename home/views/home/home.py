# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ...forms.home.home import FamilyMemberForm
from ...models import *

@login_required
def home_view(request):
    # Get the logged-in user's profile
    profile = request.user.profile
    family_members = Profile.objects.filter(family=profile.family) if profile.family else []

    # Handle form submission for adding a new family member
    if request.method == 'POST':
        form = FamilyMemberForm(request.POST)
        if form.is_valid():
            new_member = form.save(commit=False)
            new_member.family = profile.family  # Assign family to the new member
            new_member.save()
            return redirect('home')  # Redirect to avoid form resubmission

    else:
        form = FamilyMemberForm()

    context = {
        'profile': profile,
        'family_members': family_members,
        'form': form,
    }

    return render(request, 'home/home.html', context)
