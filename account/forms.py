from django import forms
from django.conf import settings
from .models import Course,Department
from .manager import UserManager
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext, ugettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
 
from django.shortcuts import get_object_or_404
GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

YEAR = (
    ('1st', 'First Year'),
    ('2nd', 'Second Year'),
    ('3rd', 'Third Year'),
    ('4rt', 'Fourth Year'),
    ('5th', 'Fifth Year')
)
class UserLoginForm(forms.Form):
    """login page"""
    email    = forms.EmailField(label='Email Address',widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def save(self):
        data     = self.cleaned_data
        email    = data['email']
        password = data['password']
        user     = authenticate(email=email, password=password)

        return user

    def clean(self, *args, **kwargs):
        email = self.data.get("email")
        password = self.data.get("password")

        if email and password:
            user_qs = User.objects.filter(email=email)

            if user_qs.count()==1:
                user = user_qs.first()
            else:
                raise forms.ValidationError("This User Does Not Exist")

            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")

            if not user.is_active:
                raise forms.ValidationError("This user is no longer active")
                
        return super(UserLoginForm, self).clean(*args, **kwargs)
        
class UserRegisterForm(forms.Form):
    """
    The form for the register page
    """
    email      = forms.EmailField(label='Email Address',widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    id_number  = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'placeholder': 'Student ID'}))
    first_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Firstname'}))
    last_name  = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Lastname'}))
    middle_initial  = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Middle Initial'}))
    gender       = forms.ChoiceField(choices = GENDER)
    course     = forms.ModelChoiceField(queryset=Course.objects.all())
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    Year       = forms.ChoiceField(choices=YEAR)
    password1 = forms.CharField(label='Password',min_length=8, widget=forms.PasswordInput(attrs={'placeholder': 'Must be at 8 characters'}), validators=[RegexValidator('^(\w+\d+|\d+\w+)+$', message="Password should be a combination of Alphabets and Numbers")])
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'placeholder': 'Must be at 8 characters'}))
    
    def save(self):
        data = self.cleaned_data

        user = User(
            email      = data['email'],
            id_number  = data['id_number'],
            first_name = data['first_name'],
            last_name  = data['last_name'],
            gender  =       data['gender'],
            middle_initial  = data['middle_initial'],
            course     = data['course'], 
            Year       = data['Year'],
            department = data['department'],

        )
        user.set_password(self.cleaned_data["password1"])
        user.is_active = True
        user.save()

        return user

    def clean_username(self):
        username    = self.data.get('username')
        username_qs = User.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError("This username has already been used")
        return username
        
    def clean_email(self):
        email    = self.data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been used")

        return email

    def clean_id_number(self):
        id_number    = self.data.get('id_number')
        id_number_qs = User.objects.filter(id_number=id_number)
        if id_number_qs.exists():
            raise forms.ValidationError("This Id Number has already been used")
        return id_number

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class EditPasswordForm(forms.Form):
    """
    Form for the currently logged in user if he/she wants to edit
    his/her password
    """
    password  = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2  = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    def save(self, user=None):
        data = self.cleaned_data
        user.password = data['password']
        user.set_password(user.password)
        user.save()


        def clean_password2(self):
            password = self.cleaned_data.get('password')
            password2 = self.cleaned_data.get('password2')

        if password2 != password:
            raise forms.ValidationError('Passwords must match')
 
class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = "__all__"

class PersonnelUserRegisterForm(forms.Form):
    """
    The form for the register page
    """
    email      = forms.EmailField(label='Email Address',widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    id_number  = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'placeholder': 'Personnel ID'}))
    first_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Firstname'}))
    last_name  = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Lastname'}))
    middle_initial  = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Middle Initial'}))
 
    department = forms.ModelChoiceField(queryset=Department.objects.all())
 
    password1 = forms.CharField(label='Password',min_length=8, widget=forms.PasswordInput(attrs={'placeholder': 'Must be at 8 characters'}), validators=[RegexValidator('^(\w+\d+|\d+\w+)+$', message="Password should be a combination of Alphabets and Numbers")])
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'placeholder': 'Must be at 8 characters'}))
    
    def save(self):
        data = self.cleaned_data

        user = User(
            email      = data['email'],
            id_number  = data['id_number'],
            first_name = data['first_name'],
            last_name  = data['last_name'],
            middle_initial  = data['middle_initial'],
            department = data['department'],

        )
        user.set_password(self.cleaned_data["password1"])
        user.is_active = True
        user.save()

        return user

    def clean_username(self):
        username    = self.data.get('username')
        username_qs = User.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError("This username has already been used")
        return username
        
    def clean_email(self):
        email    = self.data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been used")

        return email

    def clean_id_number(self):
        id_number    = self.data.get('id_number')
        id_number_qs = User.objects.filter(id_number=id_number)
        if id_number_qs.exists():
            raise forms.ValidationError("This Id Number has already been used")
        return id_number

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2