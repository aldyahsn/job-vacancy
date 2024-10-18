from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from hrd.models import Applicant


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")  # Add error message to the field
        return email


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = [
            'name', 'home_address', 'living_situation', 'sex', 'residence_phone', 'office_phone', 'mobile_phone',
            'computer_proficient', 'computer_type', 'programs_languages', 'position_applied_for',
            'interested_in_other_positions', 'current_salary', 'salary_expected', 'current_remuneration_details',
            'availability_date', 'notice_period', 'date_of_birth', 'age', 'place_of_birth', 'marital_status',
            'nationality', 'race', 'religion', 'driving_license', 'owns_car', 'good_health', 'health_issue_details',
            'serious_illness_history', 'refused_insurance_coverage', 'alcohol_or_drugs', 'alcohol_drugs_extent',
            'convicted_in_court', 'court_conviction_details', 'administrative_civil_criminal_case', 'in_debt',
            'debt_details', 'dismissed_or_suspended', 'dismissal_details', 'engaged_in_business', 'business_type',
            'other_sources_of_income', 'income_sources_details', 'spoken_languages', 'written_languages',
            'additional_language', 'hobbies_and_interests', 'additional_information', 'agreement'
        ]

        # Adding widgets for better customization
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'availability_date': forms.DateInput(attrs={'type': 'date'}),
            'marital_status': forms.RadioSelect,  # Render the field as radio buttons
            'nationality': forms.RadioSelect,  # Render the field as radio buttons
            'race': forms.RadioSelect,  # Render the field as radio buttons
            'religion': forms.RadioSelect,  # Render the field as radio buttons
            'business_type': forms.RadioSelect,  # Render the field as radio buttons
            'living_situation': forms.RadioSelect,  # Render the field as radio buttons
            'sex': forms.RadioSelect,  # Render the field as radio buttons
        }