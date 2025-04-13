from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.contrib import messages


# from django.http import HttpResponse


def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html', context)


def about(request):
    # return HttpResponse('<h2>Blog About</h2>')
    return render(request,'blog/about.html', {'title':'About'})


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = '-date_posted'

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model  = Post
    fields = [ 'title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model  = Post
    fields = [ 'title', 'content']


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Post updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        # Add an error message
        messages.error(self.request, 'There was an error updating your post.')
        return super().form_invalid(form)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def delete(self, request, *args, **kwargs):
        messages.success(request, "✅ Post deleted successfully.")
        return super().delete(request, *args, **kwargs)


