from django import forms
from .models import Post,Department,Author, Course,Memo
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.forms.widgets import FileInput

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title',
        		  'cover',
        		  'description',
        		  'author',
        		  'file')
        widgets = {
            'desciption': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
                })
        }

class ApprovePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title',
        		  'cover',
        		  'description',
        		  'author',
        		  'file',
        		  'approve')
        widgets = {
            'desciption': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
                })
        }
 
class DepartmentForm(forms.ModelForm):
	class Meta:
		model = Department
		fields = ('department_code','department_description')

class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ('course_code','course_description')

class AuthorForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = ('lastname',
				  'firstname',
				  'middlename',
				  'department',
				  'course',
				  'Year')

class MemoForm(forms.ModelForm):
	class Meta:
		model = Memo
		fields = ('title','content')