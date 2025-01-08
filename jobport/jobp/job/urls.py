#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('network', views.network, name='network'),
    path('notification', views.notification, name='notification'),
    path('profile', views.profile, name='profile'),
    path('search', views.search, name='search'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
]
