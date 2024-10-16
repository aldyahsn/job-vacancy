from django.contrib import messages
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm, ApplicantForm
from .models import Applicant, EmploymentHistory, Education, Family, Organization, ApplicantReference, Submission


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

                models_to_add_permissions = [
                    Applicant,
                    EmploymentHistory,
                    Education,
                    Family,
                    Organization,
                    ApplicantReference,
                    Submission
                ]

                # Loop through each model and assign add, view, change, and delete permissions
                for model in models_to_add_permissions:
                    content_type = ContentType.objects.get_for_model(model)

                    # Retrieve the add, view, change, and delete permissions
                    add_perm = Permission.objects.get(codename=f'add_{model._meta.model_name}', content_type=content_type)
                    view_perm = Permission.objects.get(codename=f'view_{model._meta.model_name}', content_type=content_type)
                    change_perm = Permission.objects.get(codename=f'change_{model._meta.model_name}', content_type=content_type)
                    delete_perm = Permission.objects.get(codename=f'delete_{model._meta.model_name}', content_type=content_type)

                    # Assign the permissions to the user
                    user.user_permissions.add(add_perm, view_perm, change_perm, delete_perm)

                login(request, user)
                messages.success(request, 'Registration successful! You can now log in.')
                return redirect('login')  # Redirect to login page after registration
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def applicant_create_view(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page after form submission
    else:
        form = ApplicantForm()

    return render(request, 'applicant.html', {'form': form})