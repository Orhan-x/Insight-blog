from django.shortcuts import render    


def create_post(request):
    return render(request, 'blog/create_post.html', {})