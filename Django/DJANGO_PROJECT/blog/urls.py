from django.urls import path
from .views import(
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views
urlpatterns = [
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', views.add_comment, name='add-comment'),
    path('post/<int:post_pk>/comment/<int:comment_pk>/reply/', views.add_reply, name='add-reply'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete-comment'),
    path('tag/<str:tag_name>/', views.tag_posts, name='tag-posts'),
]
