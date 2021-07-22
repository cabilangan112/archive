from django.urls import path
from . import views

app_name='account'

urlpatterns = [
    path('', views.ProfileView.as_view(), name='user'),
    path('profile/', views.ProfileAdminView.as_view(), name='user-admin'),
    path('faculty/', views.FacultyView.as_view(), name='faculty'),
    path('student/', views.StudentView.as_view(), name='student'),
    path('program_head/', views.ProfileView.as_view(), name='program'),
    path('profiles/', views.ProgramView.as_view(), name='profile'),
    path('<email>/', views.ProfileDetailView.as_view(), name='detail'),
    path('profile/edit/<int:pk>/', views.EditProfileView, name='edit_profile'),
    path('profile/assign/<email>/', views.Ruleassign, name='assign_profile'),
    path('password/edit/<id_number>/', views.EditPassword.as_view(), name='edit_password'),
]