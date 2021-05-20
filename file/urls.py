from django.urls import path 
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.static import serve
from . import views

app_name='file'

urlpatterns = [
    path('', views.PostView.as_view(), name='post'),
    path('<title>/', views.PostDetailView.as_view(), name='detail'),
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT})
    
#    path('post/', views.PdfUploadView.as_view(), name='post')
]