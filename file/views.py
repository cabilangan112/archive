import os
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.views.generic import (ListView,DetailView,CreateView,UpdateView, View)
from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)
from django.contrib.auth import get_user_model
from .models import (Post, Department, Author, Course,)
from .forms import (PostForm, DepartmentForm, CourseForm, AuthorForm)
 
class HomeView(View):
    def get(self, request, *args, **kwargs):
        file = Post.objects.all()
        context = {'file':file,}
        return render(request, "home.html", context)

class PostView(View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.all()
        context = {'post':post,}
        return render(request, "templates/pdf_list.html", context)

class PostDetailView(View):
    def get(self, request, title, *args, **kwargs):
        post = get_object_or_404(Post, title=title)
        context = {'post':post,}
        return render(request, "pdf_detail.html", context)

def download(request, path, id):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

class PdfUploadView(LoginRequiredMixin ,View):
    form_class = PostForm
    initial = {'key':'value'}
    template_name = 'template/pdf-form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('detail')
        else:
            form = PostForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)



 