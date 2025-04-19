from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Tag
from .forms import CommentForm, PostForm
from django.contrib import messages
from django.db.models import Count
import pyjokes  # Import the pyjokes library


def get_random_quote():
    """Returns a random joke from pyjokes as a quote"""
    joke = pyjokes.get_joke()  # Get a random joke
    return {
        "text": joke,
        "author": "Programmer"  # Default author for pyjokes
    }


# from django.http import HttpResponse


def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    popular_tags = Tag.objects.annotate(post_count=Count('posts')).order_by('-post_count')[:5]
    random_quote = get_random_quote()
    context = {
        'posts': Post.objects.all(),
        'popular_tags': popular_tags,
        'random_quote': random_quote
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['popular_tags'] = Tag.objects.annotate(post_count=Count('posts')).order_by('-post_count')[:5]
        context['random_quote'] = get_random_quote()
        return context


class PostDetailView(DetailView):
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Your post has been created successfully!")
        return super().form_valid(form)
        
    def form_invalid(self, form):
        messages.error(self.request, "There was an error creating your post.")
        return super().form_invalid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Post updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
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

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, id=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Your comment has been posted!")
            return redirect('post-detail', pk=post.id)
    else:
        form = CommentForm()
    
    return redirect('post-detail', pk=post.id)

@login_required
def add_reply(request, post_pk, comment_pk):
    post = get_object_or_404(Post, id=post_pk)
    parent_comment = get_object_or_404(Comment, id=comment_pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():  # Fixed extra parenthesis
            reply = form.save(commit=False)
            reply.post = post
            reply.author = request.user
            reply.parent = parent_comment
            reply.save()
            messages.success(request, "Your reply has been posted!")
    
    return redirect('post-detail', pk=post_pk)

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    post_id = comment.post.id
    
    # Check if the comment belongs to the current user
    if comment.author == request.user:
        comment.delete()
        messages.success(request, "Your comment has been deleted.")
    else:
        messages.error(request, "You cannot delete this comment.")
    
    return redirect('post-detail', pk=post_id)


def tag_posts(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = Post.objects.filter(tags=tag).order_by('-date_posted')
    popular_tags = Tag.objects.annotate(post_count=Count('posts')).order_by('-post_count')[:5]
    
    context = {
        'posts': posts,
        'popular_tags': popular_tags,
        'tag': tag
    }
    return render(request, 'blog/tag_posts.html', context)


