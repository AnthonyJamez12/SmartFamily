from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from ...models import Profile

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_onboarding')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'authentication/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # Create the associated profile
            # Automatically log the user in after registration
            login(request, user)  
            messages.success(request, 'Account created successfully.')
            return redirect('user_onboarding')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})


def about_view(request):
    return render(request, 'authentication/about.html')

