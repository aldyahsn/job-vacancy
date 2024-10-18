from django import forms
from django.contrib import admin
from fieldsets_with_inlines import FieldsetsInlineMixin

from hrd.models import Job, EmploymentHistory, Education, Family, Organization, Applicant, ApplicantReference, Submission


# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'employment_type', 'min_salary', 'max_salary', 'currency', 'is_active', 'date_posted', 'application_deadline')

    # Fields to filter the list by
    list_filter = ('employment_type', 'is_active', 'date_posted', 'application_deadline')

    # Fields to search for in the search bar
    search_fields = ('title', 'qualifications', 'skills_required', 'description', 'contact_email')

    # Fields to be grouped in the form view
    fieldsets = (
        ('Basic Job Details', {
            'fields': ('title', 'description', 'employment_type')
        }),
        ('Job Requirements', {
            'fields': ('qualifications', 'experience_required', 'skills_required')
        }),
        ('Salary and Benefits', {
            'fields': ('min_salary', 'max_salary', 'currency', 'benefits')
        }),
        ('Job Posting Details', {
            'fields': ('date_posted', 'application_deadline', 'contact_email', 'contact_phone')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )

    # Automatically populate the 'date_posted' field when a new job is added
    readonly_fields = ('date_posted',)

    # Add ordering
    ordering = ('-date_posted',)  # Most recent jobs appear first


# Applicant Admin
class EmploymentHistoryInline(admin.StackedInline):
    model = EmploymentHistory
    extra = 2
    # classes = ['collapse']

class EducationInline(admin.StackedInline):
    model = Education
    extra = 4
    # classes = ['collapse']

class FamilyInline(admin.StackedInline):
    model = Family
    extra = 3
    # classes = ['collapse']

class OrganizationInline(admin.TabularInline):
    model = Organization
    extra = 3
    # classes = ['collapse']

class ApplicantReferenceInline(admin.StackedInline):
    model = ApplicantReference
    extra = 2  # Number of extra empty forms displayed

    # Override formfield to add custom help_text based on reference type
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'reference_type':
            kwargs['help_text'] = """
                    <b>Employment:</b> From past & present employment.<br>
                    <b>Personal:</b> Give names of person of responsibility who have known you for at least 3 years.
                """
        return super().formfield_for_dbfield(db_field, request, **kwargs)

class SubmissionInline(admin.StackedInline):
    model = Submission
    extra = 2  # Number of extra empty forms displayed

    # Override formfield to add a custom label for 'company_name'
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'company_name':
            kwargs['help_text'] = "Name of companies with which you have pending applications for employment"
        return super().formfield_for_dbfield(db_field, request, **kwargs)


class ApplicantAdmin(FieldsetsInlineMixin, admin.ModelAdmin):
    list_display = ('name', 'home_address', 'good_health', 'in_debt', 'engaged_in_business', 'agreement')
    search_fields = ('name', 'home_address', 'in_debt')
    list_filter = ('good_health', 'in_debt', 'engaged_in_business')


    # Include inlines for related models
    # inlines = [EmploymentHistoryInline, EducationInline, FamilyInline, OrganizationInline]
    fieldsets_with_inlines = [
        ('BASIC INFORMATION', {
            'fields': ('name', 'home_address', 'living_situation', 'sex', 'residence_phone', 'office_phone', 'mobile_phone'),
        }),
        EducationInline,  # Inline for education placed under Basic Information

        ('COMPUTER PROFICIENCY', {
           'fields': ('computer_proficient', 'computer_type', 'programs_languages'),
        }),

        ('JOB INFORMATION', {
            'fields': ('position_applied_for', 'interested_in_other_positions', 'current_salary', 'salary_expected', 'current_remuneration_details'),
        }),

        ('AVAILABILITY', {
            'fields': ('availability_date', 'notice_period'),
            'classes': ('collapse', 'expanded'),
        }),

        ('PERSONAL INFORMATION', {
            'fields': ('date_of_birth', 'age', 'place_of_birth', 'marital_status', 'nationality', 'race', 'religion'),
            'classes': ('collapse', 'expanded'),
        }),
        EmploymentHistoryInline,  # Inline for employment history placed under Personal Information

        ('DRIVING INFORMATION', {
            'fields': ('driving_license', 'owns_car'),
            'classes': ('collapse', 'expanded'),
        }),

        ('MEDICAL DETAILS', {
            'fields': ('good_health', 'health_issue_details', 'serious_illness_history', 'refused_insurance_coverage', 'alcohol_or_drugs', 'alcohol_drugs_extent'),
            'classes': ('collapse', 'expanded'),
        }),

        ('LEGAL AND FINANCIAL HISTORY', {
            'fields': ('convicted_in_court', 'court_conviction_details', 'administrative_civil_criminal_case', 'in_debt', 'debt_details', 'dismissed_or_suspended', 'dismissal_details'),
            'classes': ('collapse', 'expanded'),
        }),
        FamilyInline,  # Inline for family placed under Legal and Financial History

        ('BUSINESS ENGAGEMENT AND OTHER INCOME', {
            'fields': ('engaged_in_business', 'business_type', 'other_sources_of_income', 'income_sources_details'),
            'classes': ('collapse', 'expanded'),
        }),

        ('LANGUAGE PROFICIENCY', {
            'fields': ('spoken_languages', 'written_languages', 'additional_language'),
            'classes': ('collapse', 'expanded'),
        }),

        ('HOBBIES AND INTERESTS', {
            'fields': ('hobbies_and_interests',),
            'classes': ('collapse', 'expanded'),
        }),
        OrganizationInline,  # Inline for organizations placed under Hobbies and Interests

        ('ADDITIONAL INFORMATION', {
            'fields': ('additional_information',),
            'classes': ('collapse', 'expanded'),
        }),

        ApplicantReferenceInline,
        SubmissionInline,
        ('AGREEMENT', {
            'fields': ('agreement',),
            'classes': ('collapse', 'expanded'),
        }),
    ]

    # Only show objects created by the currently logged-in user
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Superusers can see all records
        return qs.filter(created_by=request.user)  # Regular users can see only their own records

    # Automatically set the `created_by` field to the current user
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the object is being created, not edited
            obj.created_by = request.user
        super().save_model(request, obj, form, change)



    # fieldsets = (
    #     ('Basic Information', {
    #         'fields': ('name', 'home_address', 'living_situation', 'sex', 'residence_phone', 'office_phone', 'mobile_phone'),
    #         # 'classes': ('collapse', 'expanded'),
    #     }),
    #     ('Job Information', {
    #         'fields': ('position_applied_for', 'interested_in_other_positions', 'current_salary', 'salary_expected', 'current_remuneration_details'),
    #         # 'classes': ('collapse', 'expanded'),
    #     }),
    #     ('Availability', {
    #         'fields': ('availability_date', 'notice_period'),
    #         'classes': ('collapse', 'expanded'),
    #     }),
    #     ('Personal Information', {
    #         'fields': ('date_of_birth', 'age', 'place_of_birth', 'marital_status', 'nationality', 'race', 'religion'),
    #         'classes': ('collapse', 'expanded'),
    #     }),
    #     ('Driving Information', {
    #         'fields': ('driving_license', 'owns_car'),
    #         'classes': ('collapse', 'expanded'),
    #     }),
    #     ('Medical Details', {
    #         'fields': ('good_health', 'health_issue_details', 'serious_illness_history', 'refused_insurance_coverage', 'alcohol_or_drugs', 'alcohol_drugs_extent'),
    #         'classes': ('collapse', 'expanded'),
    #     }),
    #     ('Legal and Financial History', {
    #         'fields': ('convicted_in_court', 'court_conviction_details', 'administrative_civil_criminal_case', 'in_debt', 'debt_details', 'dismissed_or_suspended', 'dismissal_details'),
    #         'classes': ('collapse', 'expanded'),
    #     }),
    #     ('Business Engagement and Other Income', {
    #         'fields': ('engaged_in_business', 'business_type', 'other_sources_of_income', 'income_sources_details'),
    #         'classes': ('collapse', 'expanded'),
    #     }),
    #     ('Language Proficiency', {
    #         'fields': ('spoken_languages', 'written_languages', 'additional_language'),
    #         'classes': ('collapse', 'expanded'),
    #     }),
    #     ('Hobbies and Interests', {
    #         'fields': ('hobbies_and_interests',),
    #         'classes': ('collapse', 'expanded'),
    #     }),
    #     ('Additional Information', {
    #         'fields': ('additional_information',),
    #         'classes': ('collapse', 'expanded'),
    #     }),
    #     ('Agreement', {
    #         'fields': ('agreement',),
    #         'classes': ('collapse', 'expanded'),
    #     }),
    # )

    # This method customizes the form field for foreign keys in the admin
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Filter positionAppliedFor to show only active jobs
        form.base_fields['position_applied_for'].queryset = Job.objects.filter(is_active=True)
        return form


class EmploymentHistoryAdmin(admin.ModelAdmin):
    # list_display = ('applicant',)  # Display the associated applicant

    # Filter employment histories based on the logged-in user’s applicants
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Superusers can see all employment histories
        return qs.filter(applicant__created_by=request.user)  # Show only records linked to the user's applicants


class EducationAdmin(admin.ModelAdmin):
    # list_display = ('applicant',)  # Display the associated applicant

    # Filter education records based on the logged-in user’s applicants
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Superusers can see all education records
        return qs.filter(applicant__created_by=request.user)  # Show only records linked to the user's applicants

class FamilyAdmin(admin.ModelAdmin):
    # list_display = ('applicant',)  # Display the associated applicant

    # Filter education records based on the logged-in user’s applicants
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Superusers can see all education records
        return qs.filter(applicant__created_by=request.user)  # Show only records linked to the user's applicants


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('applicant',)  # Display the associated applicant

    # Filter education records based on the logged-in user’s applicants
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Superusers can see all education records
        return qs.filter(applicant__created_by=request.user)  # Show only records linked to the user's applicants



# Register all models
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(EmploymentHistory, EmploymentHistoryAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Family, FamilyAdmin)
admin.site.register(Organization, OrganizationAdmin)
