from django.shortcuts import render,redirect
from .models import User

def registration(request):
    context = {}

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create( username = username,  email = email, password = password)
        return redirect('posts')
    
    return render(request, 'register.html', context)
