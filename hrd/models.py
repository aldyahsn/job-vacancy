from django.db import models


# Create your models here.
class Job(models.Model):
    # Basic Job Details
    title = models.CharField(max_length=255, help_text="Job title, e.g., Software Engineer, Project Manager")
    description = models.TextField(help_text="Detailed job description, responsibilities, and duties")

    # Employment Type
    FULL_TIME = 'FT'
    PART_TIME = 'PT'
    CONTRACT = 'CT'
    TEMPORARY = 'TP'
    INTERNSHIP = 'IN'

    EMPLOYMENT_TYPE_CHOICES = [
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
        (CONTRACT, 'Contract'),
        (TEMPORARY, 'Temporary'),
        (INTERNSHIP, 'Internship'),
    ]

    employment_type = models.CharField(
        max_length=2,
        choices=EMPLOYMENT_TYPE_CHOICES,
        default=FULL_TIME,
        help_text="Type of employment"
    )

    # Job Requirements
    qualifications = models.TextField(blank=True, help_text="Required qualifications, degrees, or certifications")
    experience_required = models.PositiveIntegerField(help_text="Minimum years of experience required", default=0)
    skills_required = models.TextField(blank=True, help_text="Required skills for this position")

    # Salary and Benefits
    min_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Minimum salary offered")
    max_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Maximum salary offered")
    currency = models.CharField(max_length=3, default='USD', help_text="Currency of the salary, e.g., USD, EUR, IDR")
    benefits = models.TextField(blank=True, help_text="Additional benefits such as health insurance, paid leave, etc.")

    # Job Posting Details
    date_posted = models.DateField(auto_now_add=True, help_text="Date when the job was posted")
    application_deadline = models.DateField(blank=True, null=True, help_text="Application deadline")
    contact_email = models.EmailField(help_text="Contact email for job applications")
    contact_phone = models.CharField(max_length=20, blank=True, null=True, help_text="Contact phone number for job applications")

    # Status
    is_active = models.BooleanField(default=True, help_text="Is this job posting currently active?")

    def __str__(self):
        return self.title


class Applicant(models.Model):
    # Basic Information
    name = models.CharField(max_length=255)
    home_address = models.TextField()

    # Living Situation
    OWN_HOUSE = 'Own house'
    RENTED_HOUSE = 'Rented house'
    WITH_PARENTS = 'With parents'
    OTHERS = 'Others'
    LIVING_CHOICES = [
        (OWN_HOUSE, 'Own house'),
        (RENTED_HOUSE, 'Rented house'),
        (WITH_PARENTS, 'With parents'),
        (OTHERS, 'Others'),
    ]
    living_situation = models.CharField(max_length=20, choices=LIVING_CHOICES)

    # Sex and Contact Info
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    residence_phone = models.CharField(max_length=20, blank=True, null=True)
    office_phone = models.CharField(max_length=20, blank=True, null=True)
    mobile_phone = models.CharField(max_length=20)

    # Computer Proficiency
    computer_proficient = models.BooleanField()
    computer_type = models.CharField(max_length=255, blank=True, null=True)
    programs_languages = models.TextField(blank=True, null=True)

    # Job Information
    position_applied_for = models.ForeignKey(Job, on_delete=models.CASCADE, help_text="Job the applicant applied for")
    interested_in_other_positions = models.BooleanField()
    current_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    salary_expected = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    current_remuneration_details = models.TextField(blank=True, null=True)

    # Availability and Notice Period
    availability_date = models.DateField(blank=True, null=True)
    notice_period = models.CharField(max_length=50, blank=True, null=True)

    # Personal Information
    date_of_birth = models.DateField()
    age = models.PositiveIntegerField()
    place_of_birth = models.CharField(max_length=255)

    # Marital Status Choices
    SINGLE = 'Single'
    MARRIED = 'Married'
    DIVORCED = 'Divorced'
    WIDOWED = 'Widowed'

    MARITAL_STATUS_CHOICES = [
        (SINGLE, 'Belum Menikah (Single)'),
        (MARRIED, 'Menikah (Married)'),
        (DIVORCED, 'Cerai (Divorced)'),
        (WIDOWED, 'Janda/Duda (Widowed)'),
    ]

    marital_status = models.CharField(max_length=50, choices=MARITAL_STATUS_CHOICES)

    # Nationality Choices (Using common nationalities, but you can adjust as needed)
    INDONESIAN = 'ID'
    FOREIGNER = 'FR'

    NATIONALITY_CHOICES = [
        (INDONESIAN, 'Warga Negara Indonesia (Indonesian)'),
        (FOREIGNER, 'Warga Negara Asing (Foreigner)'),
    ]

    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES)

    # Race Choices (Commonly used terms in Indonesia)
    JAWA = 'Jawa'
    SUNDA = 'Sunda'
    BETAWI = 'Betawi'
    BATAK = 'Batak'
    CHINESE_INDONESIAN = 'Tionghoa'
    OTHER = 'Other'

    RACE_CHOICES = [
        (JAWA, 'Jawa'),
        (SUNDA, 'Sunda'),
        (BETAWI, 'Betawi'),
        (BATAK, 'Batak'),
        (CHINESE_INDONESIAN, 'Tionghoa'),
        (OTHER, 'Lainnya (Other)'),
    ]

    race = models.CharField(max_length=100, choices=RACE_CHOICES)

    # Religion Choices (Based on the recognized religions in Indonesia)
    ISLAM = 'Islam'
    CATHOLIC = 'Catholic'
    CHRISTIAN = 'Christian'
    HINDU = 'Hindu'
    BUDDHA = 'Buddha'
    CONFUCIANISM = 'Confucianism'
    OTHER_RELIGION = 'Other'

    RELIGION_CHOICES = [
        (ISLAM, 'Islam'),
        (CATHOLIC, 'Katolik (Catholic)'),
        (CHRISTIAN, 'Kristen (Christian)'),
        (HINDU, 'Hindu'),
        (BUDDHA, 'Buddha'),
        (CONFUCIANISM, 'Konghucu (Confucianism)'),
        (OTHER_RELIGION, 'Lainnya (Other)'),
    ]

    religion = models.CharField(max_length=100, choices=RELIGION_CHOICES)

    # Driving Information
    driving_license = models.CharField(max_length=50, blank=True, null=True)
    owns_car = models.BooleanField()

    # Medical Details
    good_health = models.BooleanField()
    health_issue_details = models.TextField(blank=True, null=True, help_text="If not in good health, specify reasons.")
    serious_illness_history = models.TextField(blank=True, null=True, help_text="Provide details of serious illness, allergies, operations, disabilities, or accidents with dates.")

    refused_insurance_coverage = models.BooleanField()
    alcohol_or_drugs = models.BooleanField()
    alcohol_drugs_extent = models.TextField(blank=True, null=True, help_text="Specify the extent of alcohol/drug consumption.")

    convicted_in_court = models.BooleanField()
    court_conviction_details = models.TextField(blank=True, null=True, help_text="If convicted, provide details.")

    administrative_civil_criminal_case = models.TextField(blank=True, null=True, help_text="Provide details if involved in any cases.")
    in_debt = models.BooleanField()
    debt_details = models.TextField(blank=True, null=True, help_text="If in debt, provide details including to whom, the extent, and reason.")

    dismissed_or_suspended = models.BooleanField()
    dismissal_details = models.TextField(blank=True, null=True, help_text="If dismissed or suspended, provide details.")

    engaged_in_business = models.BooleanField()
    # Business Type Choices (Common Indonesian business sectors)
    RETAIL = 'Retail'
    MANUFACTURING = 'Manufacturing'
    AGRICULTURE = 'Agriculture'
    CONSTRUCTION = 'Construction'
    FINANCE = 'Finance'
    HEALTHCARE = 'Healthcare'
    EDUCATION = 'Education'
    HOSPITALITY = 'Hospitality'
    TRANSPORTATION = 'Transportation'
    IT_TECH = 'IT/Tech'
    OTHER_BUSINESS = 'Other'

    BUSINESS_TYPE_CHOICES = [
        (RETAIL, 'Perdagangan (Retail)'),
        (MANUFACTURING, 'Manufaktur (Manufacturing)'),
        (AGRICULTURE, 'Pertanian (Agriculture)'),
        (CONSTRUCTION, 'Konstruksi (Construction)'),
        (FINANCE, 'Keuangan (Finance)'),
        (HEALTHCARE, 'Kesehatan (Healthcare)'),
        (EDUCATION, 'Pendidikan (Education)'),
        (HOSPITALITY, 'Perhotelan (Hospitality)'),
        (TRANSPORTATION, 'Transportasi (Transportation)'),
        (IT_TECH, 'Teknologi Informasi (IT/Tech)'),
        (OTHER_BUSINESS, 'Lainnya (Other)'),
    ]

    business_type = models.CharField(max_length=255, choices=BUSINESS_TYPE_CHOICES, blank=True, null=True, help_text="If engaged in business, specify the type.")

    other_sources_of_income = models.BooleanField()
    income_sources_details = models.TextField(blank=True, null=True, help_text="If other sources of income, provide details.")

    # Language Proficiency
    INDONESIAN = 'IN'
    ENGLISH = 'EN'
    CHINESE = 'CH'
    OTHER = 'OT'

    LANGUAGE_CHOICES = [
        (INDONESIAN, 'Indonesian'),
        (ENGLISH, 'English'),
        (CHINESE, 'Chinese'),
        (OTHER, 'Other'),
    ]

    spoken_languages = models.CharField(max_length=3, choices=LANGUAGE_CHOICES, default=INDONESIAN)
    written_languages = models.CharField(max_length=3, choices=LANGUAGE_CHOICES, default=INDONESIAN)
    additional_language = models.CharField(max_length=255, blank=True, null=True, help_text="Specify if any other language spoken/written.")

    # Hobbies and Interests
    hobbies_and_interests = models.TextField(blank=True, null=True, help_text="List hobbies, games, or other interests.")

    # Additional Information
    additional_information = models.TextField(blank=True, null=True, help_text="Any additional information for the employer, including why you are suitable for the position.")

    agreement = models.BooleanField("Agree",
        default=False,
        help_text="I HEREBY CONFIRM ALL THE ABOVE DETAILS TO BE TRUE AND CORRECT.<br>"
                  "I AUTHORISE {{ COMPANY }}TO CARRY OUT. REFERENCE CHECK WITH PAST EMPLOYER AND REFEREES IN CONNECTION WITH THIS APPLICATION.<br>"
                  "I UNDERSTAND THAT ANY MISPRESENTATION OR MISSION OF INFORMATION WILL BE SUFFICIENT REASONS "
                  "FOR WITHDRAWL OF AN OFFER OR SUBSEQUENT DISMISSAL, IF EMPLOYED"
    )

def __str__(self):
    return self.name


class EmploymentHistory(models.Model):
    # Foreign Key to Applicant
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='employment_histories')

    # Employment Period
    date_of_employment = models.DateField()
    date_employment_ended = models.DateField(blank=True, null=True)  # This can be null if still employed

    # Company Information
    company_name = models.CharField(max_length=255)
    company_address = models.TextField()

    # Job Details
    nature_of_business = models.CharField(max_length=255)
    position_held = models.CharField(max_length=255)
    supervisor_name = models.CharField(max_length=255)
    supervisor_designation = models.CharField(max_length=255)

    # Employee Information
    total_employees_in_company = models.PositiveIntegerField(blank=True, null=True)
    number_of_staff_supervised = models.PositiveIntegerField(blank=True, null=True)

    # Responsibilities
    description_of_duties = models.TextField()

    # Additional Information
    employed_through = models.CharField(max_length=255, help_text="How did you get employed? (e.g., Advertisement, Recommendation)")
    reason_for_leaving = models.CharField(max_length=255, blank=True, null=True)
    last_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.company_name} ({self.position_held})"


class Education(models.Model):
    # ForeignKey to Applicant
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='education_records')

    # Education Period (Year only)
    from_year = models.PositiveIntegerField()
    to_year = models.PositiveIntegerField(blank=True, null=True)  # Can be blank if still studying

    # School/College Information
    school_name = models.CharField(max_length=255)

    # State Level Attained Choices (Indonesian Education Levels)
    SD = 'SD'
    SMP = 'SMP'
    SMA = 'SMA'
    DIPLOMA = 'DIP'
    S1 = 'S1'
    S2 = 'S2'
    S3 = 'S3'

    STATE_LEVEL_CHOICES = [
        (SD, 'Sekolah Dasar (SD)'),
        (SMP, 'Sekolah Menengah Pertama (SMP)'),
        (SMA, 'Sekolah Menengah Atas (SMA)'),
        (DIPLOMA, 'Diploma'),
        (S1, 'Sarjana (S1)'),
        (S2, 'Magister (S2)'),
        (S3, 'Doktor (S3)'),
    ]

    state_level_attained = models.CharField(
        max_length=3,
        choices=STATE_LEVEL_CHOICES,
        default=SD
    )

    major_course = models.CharField(max_length=255)  # Major course/subject

    def __str__(self):
        return f"{self.school_name} ({self.from_year} - {self.to_year})"


class Organization(models.Model):
    # ForeignKey to Applicant
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='organizations')

    # Organization Membership Period (Year only)
    from_year = models.PositiveIntegerField()
    to_year = models.PositiveIntegerField(blank=True, null=True)  # Can be blank if still a member

    # Organization Details
    organization_name = models.CharField(max_length=255)
    position_held = models.CharField(max_length=255, blank=True, null=True)  # Position held in the organization

    def __str__(self):
        return f"{self.organization_name} ({self.from_year} - {self.to_year})"


class Family(models.Model):
    # ForeignKey to Applicant
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='family_members')

    # Family Details
    FATHER = 'Father'
    MOTHER = 'Mother'
    BROTHER = 'Brother'
    SISTER = 'Sister'
    SPOUSE = 'Spouse'
    CHILD = 'Child'

    RELATIONSHIP_CHOICES = [
        (FATHER, 'Father'),
        (MOTHER, 'Mother'),
        (BROTHER, 'Brother'),
        (SISTER, 'Sister'),
        (SPOUSE, 'Spouse'),
        (CHILD, 'Child'),
    ]

    relationship = models.CharField(max_length=10, choices=RELATIONSHIP_CHOICES)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    employer_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.relationship}: {self.name}"


class ApplicantReference(models.Model):
    # Type Choices for Reference
    EMPLOYMENT = 'Employment'
    PERSONAL = 'Personal'

    REFERENCE_TYPE_CHOICES = [
        (EMPLOYMENT, 'Employment'),
        (PERSONAL, 'Personal'),
    ]
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='references')

    # Reference type (Employment or Personal)
    reference_type = models.CharField(max_length=20, choices=REFERENCE_TYPE_CHOICES, help_text="Type of reference: Employment or Personal")

    # Basic Information for the Applicant Reference
    name = models.CharField(max_length=255, help_text="Name of the reference")
    position = models.CharField(max_length=255, help_text="Position of the reference")
    company_name = models.CharField(max_length=255, help_text="Company name where the reference works")
    company_address = models.TextField(help_text="Company address of the reference")

    # Contact Information
    office_phone = models.CharField(max_length=20, blank=True, null=True, help_text="Office phone number")
    residence_phone = models.CharField(max_length=20, blank=True, null=True, help_text="Residence phone number")

    # Years of Acquaintance
    years_of_acquaintance = models.PositiveIntegerField(help_text="Number of years the applicant has known the reference")

    def __str__(self):
        return f"{self.name} ({self.reference_type})"

class Submission(models.Model):
    # ForeignKey to Applicant
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='submissions')

    # Submission for company with a pending application
    company_name = models.CharField(max_length=255, help_text="Name of the company with a pending application")
    date_of_application = models.DateField(help_text="Date of application for the company")

    def __str__(self):
        return f"Submission for {self.company_name} on {self.date_of_application}"
