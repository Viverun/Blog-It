from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

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
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = '-date_posted'