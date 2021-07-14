from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings
from .validators import validate_file_extention
from django.urls import reverse
from django.db.models import Q
from .utils import unique_slug_generator
from account.models import Course,Department
User = settings.AUTH_USER_MODEL

YEAR = (
    ('1st', 'Firs Year'),
    ('2nd', 'Second Year'),
    ('3rd', 'Third Year'),
    ('4rt', 'Fourth Year'),
    ('grad', 'Graduate'),
    
)

TYPE = (
    ('Memorandum', 'Memorandum'),
    ('Research', 'Research'),
    ('Syllabus', 'Syllabus'),
    ('Curriculum', 'Curriculum'),
) 
class FileQuerySet(models.query.QuerySet):
    def search(self,query): 
        if query:
            query = query.strip()
            return self.filter(
                Q(title__icontains=query)
 

                ).distinct()
        return self
 
class FileManager(models.Manager):
    def get_queryset(self):
        return FileQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)



def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class PathAndRename(object):

    def __init__(self,sub_path):
        self.path = sub_path

    def __call__(self,instance, filename):
        ext = filename.split('.')[-1]

        if instance.pk:
            filename = '{}.{}'.format(instance.pk,ext)
        else:
            filename = '{}.{}'.format(instance.pk,ext)
        return os.path.join(self.path, filename)

path_and_rename = PathAndRename("media/file/")

class Author(models.Model):
    lastname           = models.CharField(max_length=100)
    firstname          = models.CharField(max_length=100)
    middlename         = models.CharField(max_length=100)
    email              = models.EmailField(max_length=254)
    department         = models.ForeignKey(Department, null=True,on_delete=models.CASCADE)
    course             = models.ForeignKey(Course, null=True,on_delete=models.CASCADE)
    Year               = models.CharField(max_length=6, choices=YEAR, blank=True, default=True)
    date_created       = models.DateTimeField(auto_now_add = True)
    date_modified      = models.DateTimeField(auto_now = True)
    slug               = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.lastname)

    class Meta:
        ordering = ['-id']

class Post(models.Model):
    title          = models.CharField(max_length=100)
    type_documents = models.CharField(max_length=30, choices=YEAR, blank=True, default=True)   
    description    = models.TextField(null=True, blank=True)
    author         = models.ForeignKey(Author, null=True,on_delete=models.CASCADE)
    date_uploaded  = models.DateTimeField(auto_now_add=True)
    modified       = models.DateTimeField(auto_now=True)
    file           = models.FileField(null=True,validators=[PathAndRename] )
 
    
    approve        = models.BooleanField(default=False)
    remove         = models.BooleanField(default=False)

    objects = FileManager()

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['-date_uploaded']

class Memo(models.Model):

    title          = models.CharField(max_length=100)
    content        = models.FileField(upload_to="content", null=True)
    date_uploaded  = models.DateTimeField(auto_now_add=True)
    modified       = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)
        
    @property
    def slug_title(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['-date_uploaded']
