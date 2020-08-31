from django.shortcuts import render
from django.http import HttpResponse
from .models import Story

from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, DetailView

def home_view(request, *args, **kwargs):
    obj = Story.objects.all()
    context = {
        'objects': obj,
    }
    return render(request, 'questions/index.html', context)

class AdminLoginView(LoginView):
    def login_auth(request):
        if request.user.is_authenticated:
            return redirect('create-story')
        else: 
            pass

        return login_auth 

class StoryDetailView(DetailView):
    model = Story

class StoryCreateView(CreateView):
    model = Story
    fields = ['title', 'content', 'instruction']
