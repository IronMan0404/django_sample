from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'homepage.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def logout(request):
    return render(request, 'logout.html')


def base(request):
    return render(request, 'base.html')


def contact(request):
    return render(request, 'contact.html')
    
def about(request):
    return render(request, 'about.html')