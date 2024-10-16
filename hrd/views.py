from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already in use. Please choose a different email.')
            else:
                # Create and save the new user
                user = form.save(commit=False)  # Don't save to the database yet
                user.is_staff = True  # Set user as staff
                user.save()  # Save the user to the database
                login(request, user)
                messages.success(request, 'Registration successful! You can now log in.')
                return redirect('login')  # Redirect to login page after registration
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})