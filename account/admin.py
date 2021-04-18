from django.contrib import admin
from .models import Course,Department,User,Confirmation

admin.site.register(Course)
admin.site.register(Department)
admin.site.register(User)
admin.site.register(Confirmation)

