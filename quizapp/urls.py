"""quizapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from questions.views import (home_view, 
    AdminLoginView,  
    StoryCreateView,
    StoryDetailView,
    StoryUpdateView,
    StoryDeleteView
)
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home-page'),
    path('create/', StoryCreateView.as_view(), name='create-story'),
    path('story/<int:pk>', StoryDetailView.as_view(), name='story-detail'),
    path('story/<int:pk>/update/', StoryUpdateView.as_view(), name='story-update'),
    path('story/<int:pk>/delete/', StoryDeleteView.as_view(), name='story-delete'),
    path('login/', AdminLoginView.as_view(template_name='questions/login.html'), name='admin-login'),
    path('logout/', LogoutView.as_view(template_name='questions/logout.html'), name='logout'),
]
