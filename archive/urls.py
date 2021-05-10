"""archive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from file.views import HomeView
from django.conf import settings
from django.urls import path, include, reverse_lazy
from account.views import LoginView, RegisterView,PersonnelRegisterView
from django.contrib.auth.views import  LogoutView
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),

    path('account/', include('account.urls', namespace='user')),
    path('file/', include('file.urls', namespace='file')),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    path('register/',RegisterView.as_view(), name='register'),
    path('register-personnel/',PersonnelRegisterView.as_view(), name='register-personnel'),

]
urlpatterns.extend(
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
