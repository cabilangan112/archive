import os
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)
from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.views.generic import (ListView,DetailView,CreateView,UpdateView, View)
from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)
from django.contrib.auth import get_user_model
from .models import (Post, Department, Author, Course,)
from .forms import (PostForm, DepartmentForm, CourseForm, AuthorForm)
 
class HomeView(View):
    def get(self, request, *args, **kwargs):
        file = Post.objects.all()[:9]
        context = {'file':file,}
        return render(request, "home.html", context)

class PostView(View):
    def get(self, request, *args, **kwargs):
        file = Post.objects.all()
        context = {'file':file,}
        return render(request, "file_list.html", context)

class PostDetailView(LoginRequiredMixin,View):
    def get(self, request, title, *args, **kwargs):
        post = get_object_or_404(Post, title=title)
        context = {'post':post,}
        return render(request, "file_detail.html", context)

def download(request, path, id):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def uploadFile(request):
    if request.method == 'POST':
        filename = request.POST['filename']
        owner = request.POST['owner']
        pdf = request.FILES['pdf']
        cover = request.FILES['cover']

        a = Files(filename=filename, owner=owner, pdf=pdf, cover=cover)
        a.save()
        messages.success(request, 'Files Submitted successfully!')
        return redirect('files')
    else:
        messages.error(request, 'Files was not Submitted successfully!')
        return redirect('form')

