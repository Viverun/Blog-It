"""
URL configuration for DJANGO_PROJECT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('blog/', include('blog.urls')),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('user/<str:username>/', user_views.user_profile, name='user-profile'),
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"),
         name="login"),
    # path("logout/", auth_views.LogoutView.as_view(template_name="users/logout.html", http_method_names=['get', 'post']),
    #      name="logout"),
    path("logout/", user_views.custom_logout, name="logout"),
    # Remove or comment out the previous logout path
    #path("logout/", auth_views.LogoutView.as_view(template_name="users/logout.html"...
    path('', include('blog.urls')),
    path('summernote/', include('django_summernote.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
