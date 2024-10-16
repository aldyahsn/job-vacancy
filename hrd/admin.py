from django.contrib import admin

from hrd.models import Job, EmploymentHistory, Education, Family, Organization, Applicant


# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass


# Applicant Admin
class EmploymentHistoryInline(admin.TabularInline):
    model = EmploymentHistory
    extra = 1
    classes = ['collapse']

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1
    classes = ['collapse']

class FamilyInline(admin.TabularInline):
    model = Family
    extra = 1
    classes = ['collapse']

class OrganizationInline(admin.TabularInline):
    model = Organization
    extra = 1
    classes = ['collapse']


class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'home_address', 'good_health', 'in_debt', 'engaged_in_business', 'agreement')
    search_fields = ('name', 'home_address', 'in_debt')
    list_filter = ('good_health', 'in_debt', 'engaged_in_business')

    # Include inlines for related models
    inlines = [EmploymentHistoryInline, EducationInline, FamilyInline, OrganizationInline]

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'home_address', 'living_situation', 'sex', 'residence_phone', 'office_phone', 'mobile_phone'),
            # 'classes': ('collapse', 'expanded'),
        }),
        ('Job Information', {
            'fields': ('position_applied_for', 'interested_in_other_positions', 'current_salary', 'salary_expected', 'current_remuneration_details'),
            # 'classes': ('collapse', 'expanded'),
        }),
        ('Availability', {
            'fields': ('availability_date', 'notice_period'),
            'classes': ('collapse', 'expanded'),
        }),
        ('Personal Information', {
            'fields': ('date_of_birth', 'age', 'place_of_birth', 'marital_status', 'nationality', 'race', 'religion'),
            'classes': ('collapse', 'expanded'),
        }),
        ('Driving Information', {
            'fields': ('driving_license', 'owns_car'),
            'classes': ('collapse', 'expanded'),
        }),
        ('Medical Details', {
            'fields': ('good_health', 'health_issue_details', 'serious_illness_history', 'refused_insurance_coverage', 'alcohol_or_drugs', 'alcohol_drugs_extent'),
            'classes': ('collapse', 'expanded'),
        }),
        ('Legal and Financial History', {
            'fields': ('convicted_in_court', 'court_conviction_details', 'administrative_civil_criminal_case', 'in_debt', 'debt_details', 'dismissed_or_suspended', 'dismissal_details'),
            'classes': ('collapse', 'expanded'),
        }),
        ('Business Engagement and Other Income', {
            'fields': ('engaged_in_business', 'business_type', 'other_sources_of_income', 'income_sources_details'),
            'classes': ('collapse', 'expanded'),
        }),
        ('Language Proficiency', {
            'fields': ('spoken_languages', 'written_languages', 'additional_language'),
            'classes': ('collapse', 'expanded'),
        }),
        ('Hobbies and Interests', {
            'fields': ('hobbies_and_interests',),
            'classes': ('collapse', 'expanded'),
        }),
        ('Additional Information', {
            'fields': ('additional_information',),
            'classes': ('collapse', 'expanded'),
        }),
        ('Agreement', {
            'fields': ('agreement',),
            'classes': ('collapse', 'expanded'),
        }),
    )

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
