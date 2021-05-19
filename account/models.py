from django.db import models
from django.conf import settings 
from django.urls import reverse

import uuid

from .manager import UserManager
from django.contrib.auth.models import (
     BaseUserManager, AbstractBaseUser,PermissionsMixin
)

YEAR = (
    ('1st', 'Firs Year'),
    ('2nd', 'Second Year'),
    ('3rd', 'Third Year'),
    ('4th', 'Fourth Year'),
    ('5th', 'Fifth Year'),
    ('Personnel', 'Personnel'),
)
class Course(models.Model):
    course_code        = models.CharField(max_length=100)
    course_description = models.CharField(max_length=100, null=True) 
    date_created       = models.DateTimeField(auto_now_add=True)
    date_modified      = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.course_code)

    @property
    def slug_title(self):
        return '{}'.format(self.course_code )   

    class Meta:
        ordering = ['-date_created']

class Department(models.Model):
    department_code        = models.CharField(max_length=100)
    department_description = models.CharField(max_length=100) 
    date_created           = models.DateTimeField(auto_now_add=True)
    date_modified          = models.DateTimeField(auto_now=True)
    slug                   = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.department_code)
        
    @property
    def slug_title(self):
        return '{}'.format(self.department_code)   

    class Meta:
        ordering = ['-date_created']

class User(AbstractBaseUser):
    """ user model
    """
    email        = models.EmailField(max_length=500, unique=True)
    id_number    = models.CharField(max_length=80)
    first_name   = models.CharField(max_length=80)
    last_name    = models.CharField(max_length=80)
    middle_initial = models.CharField(max_length=80)
    course       = models.ForeignKey(Course, null=True, blank=True, on_delete = models.CASCADE)
    Year         = models.CharField(max_length=30, choices=YEAR, blank=True, default=True)
    department   = models.ForeignKey(Department, null=True, blank=True, on_delete = models.CASCADE)

    Faculty 	 = models.BooleanField(default=False)
    Program_head = models.BooleanField(default=False)
    Dean         = models.BooleanField(default=False)
    is_staff     = models.BooleanField(default=False)
    Students     = models.BooleanField(default=False)
    quality_assurance = models.BooleanField(default=False)
    is_active 	 = models.BooleanField(default=True)

    date_joined  = models.DateTimeField(auto_now_add=True) 
    date_updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("first_name", "last_name")

    objects = UserManager()
 
    def __str__(self):
        return f"{self.email}"

    class Meta:
        ordering = ['-last_name']

    def save(self, *args, **kwargs):
        if not self.id:
            self.handle = self.trimmed_email

        return super(User, self).save(*args, **kwargs)

    def get_short_name(self):
        return f"{self.first_name}"

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".title()

    @property
    def get_display_name(self):
        if self.first_name and self.last_name:
            return self.get_full_name
        return f"{self.email}"

    @property
    def trimmed_email(self):
        return self.email.split("@")[0]

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

class Confirmation(models.Model):
    """ change password confirmation model
    """
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    url = models.CharField(max_length=500, default='')
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        self.url = reverse('users:changepass', args={str(self.id)})

        return super(Confirmation, self).save(*args, **kwargs)

