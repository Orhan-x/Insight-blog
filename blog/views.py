from django.shortcuts import render 
from .forms import PostForm



def create_post(request):
    context  = {}
    if request.method == "POST":
        # logic stuff
        pass
    context['form'] = PostForm()
    return render(request, 'blog/create_post.html', context)

# Home page and also Posts pages
def home(request):
    return render(request, 'blog/home.html', {})