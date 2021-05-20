import os
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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
        query = self.request.GET.get('q')
        file = Post.objects.all().order_by("-title").search(query)
        
        if file.exists():
            return render(request, "file/file_list.html",{'file':file})
        return render(request, "file/file_list.html",{'file':file})

class PostDetailView(LoginRequiredMixin,View):
    def get(self, request, title, *args, **kwargs):
        post = get_object_or_404(Post, title=title)
        context = {'post':post,}
        return render(request, "file/file_detail.html", context)


class AuthorView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        author = Author.objects.all().order_by("-title").search(query)
        
        if author and qs.exists():
            return render(request, "author_list.html",{'author':author})
        return render(request, "author_list.html",{'author':author})

class AuthorDetailView(LoginRequiredMixin,View):
    def get(self, request, lastname, *args, **kwargs):
        author = get_object_or_404(Author, lastname=lastname)
        context = {'author':author,}
        return render(request, "file_detail.html", context)


def AdminAproval(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = pprovePostForm(request.POST, instance=Post )
        if form.is_valid():           
            post = form.save(commit=False)
            post.save()
        return redirect('file:post')
    else:
        form = pprovePostForm(instance=Post)
    return render(request, 'post/approve-form.html',{'form': form,
        'post':post})


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/file")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

