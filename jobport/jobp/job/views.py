from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'home.html')

def network(request):
    return render(request,'network.html')

def notification(request):
    return render(request, 'notification.html')

def profile(request):
    return render(request, 'profile.html')

def search(request):
    return render(request, 'search.html')

def signin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        messages.error(request, 'Invalid email or password.')
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')