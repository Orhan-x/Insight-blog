from django.shortcuts import render
from .forms import PostForm

def home(request):
    
    context = {}
    
    return render(request, 'blog/home.html', context)


def create_post(request):
    context = {}
    
    if request.method == "GET":
        form = PostForm()
        context['form'] = form
        return render(request, 'blog/create_post.html', context)
    if request.method == 'POST':
        pass
    
