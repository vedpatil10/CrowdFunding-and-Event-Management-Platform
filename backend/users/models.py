from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    """Custom User model for the crowdfunding platform"""
    
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('committee', 'Committee Member'),
        ('admin', 'Admin'),
    ]
    
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='student')
    college_name = models.CharField(max_length=200, blank=True)
    student_id = models.CharField(max_length=50, blank=True)
    is_verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return f"{self.username} ({self.email})"
    
    class Meta:
        db_table = 'users'
