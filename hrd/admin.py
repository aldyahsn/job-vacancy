from django.contrib import admin
from fieldsets_with_inlines import FieldsetsInlineMixin

from hrd.models import Job, EmploymentHistory, Education, Family, Organization, Applicant, ApplicantReference, Submission


# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass


# Applicant Admin
class EmploymentHistoryInline(admin.StackedInline):
    model = EmploymentHistory
    extra = 2
    # classes = ['collapse']

class EducationInline(admin.StackedInline):
    model = Education
    extra = 3
    # classes = ['collapse']

class FamilyInline(admin.StackedInline):
    model = Family
    extra = 1
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


# Register all models
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(EmploymentHistory)
admin.site.register(Education)
admin.site.register(Family)
admin.site.register(Organization)
