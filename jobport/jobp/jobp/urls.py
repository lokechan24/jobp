# In your project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('job.urls')),  # Your app URLs
    path('admin/', admin.site.urls),
]
