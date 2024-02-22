from django.shortcuts import render,redirect
from .forms import RegistrationForm

def registration(request):
    context = {}
    if request.method == "GET":
        return render(request, 'register.html', context)
    if request.method == "POST":
        

        return redirect('posts', 1)
