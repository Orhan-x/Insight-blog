from django.shortcuts import render
from .forms import RegistrationForm

def registration(request):
    context = {}
    if request.method == "GET":
        form = RegistrationForm()
        context["form"] = form
        pass
    return render(request, 'register.html', context)
