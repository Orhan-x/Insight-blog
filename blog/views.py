from django.shortcuts import render , redirect
from .forms import PostForm



def create_post(request):
    context  = {}
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    context['form'] = PostForm()
    return render(request, 'blog/create_post.html', context)

# Home page and also Posts pages
def home(request):
    return render(request, 'blog/home.html', {})