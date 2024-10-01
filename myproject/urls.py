from django.contrib import admin
from django.urls import path
from hello.views import hello_world  # Import your view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),  # Add the path to your hello_world view
]
