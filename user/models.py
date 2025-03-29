from django.contrib.auth.models import AbstractUser
from django.db import models

class UserAccount(AbstractUser):  
    USER_TYPES = [
        ('applicant', 'Applicant'),
        ('employer', 'Employer'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    # For All Users
    first_name = models.CharField(max_length=255, blank= True, null= True)
    last_name = models.CharField(max_length=255, blank= True, null= True)

    # Only For Applicant

    # Only for Employers
    company_name = models.CharField(max_length=255, blank=True, null=True)  

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
