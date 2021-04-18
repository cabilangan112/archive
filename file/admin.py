from django.contrib import admin
from .models import Course,Department,Author,Post

# Register your models here.

admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Author)
admin.site.register(Post)