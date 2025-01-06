from django.shortcuts import render
from django.http import HttpResponse
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
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')