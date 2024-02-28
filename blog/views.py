from django.shortcuts import render    


def create_post(request):
    return render(request, 'blog/create_post.html', {})

# Home page and also Posts pages
def home(request):
    return render(request, 'blog/home.html', {})