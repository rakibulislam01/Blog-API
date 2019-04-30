"""mainBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url, include
from django.conf import urls
from django.conf import settings
from django.conf.urls.static import static
from blogApp import views
# from blogApp.api import urls
from accounts.views import (login_view,
                            register_view,
                            logout_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogApp/', include('blogApp.urls')),
    path('comments/', include('comments.urls')),
    # url(r'^login/', login_view, name='login'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register', register_view, name='register'),
    # url(r'^reviews/', include(('reviews.urls', 'reviews'), namespace='reviews')),
    path('', views.post_list, name="posts"),
    path('api/posts/', include('blogApp.api.urls')),
    path('api/comments/', include('comments.api.urls')),
    path('api/users/', include('accounts.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
