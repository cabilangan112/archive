from django.urls import path 
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.static import serve
from . import views

app_name='file'

urlpatterns = [
    path('', views.PostView.as_view(), name='post'),
    path('admin-list/', views.PostAdminView.as_view(), name='post-admin'),
    path('memo/', views.Memorandum.as_view(), name='memo'),
    path('memo-admin/', views.MemoAdmin.as_view(), name='memo-admin'),
    path('curriculum/', views.Curriculum.as_view(), name='curriculum'),
    path('Syllabus', views.Syllabus.as_view(), name='syllabus'),
    path('<title>/', views.PostDetailView.as_view(), name='detail'),
    path('memo/<title>/', views.MemoDetailView.as_view(), name='memo-detail'),
    path('approve-file/<int:pk>/', views.AdminAproval, name='file-approve'),
    path('approve-memo/<int:pk>/', views.MemoApprove, name='memo-approve'),
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT})
   
#    path('post/', views.PdfUploadView.as_view(), name='post')
]