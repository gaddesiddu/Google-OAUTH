from django.contrib import admin
from django.urls import path, include
from social import views  # Import your view function

urlpatterns = [
    path('',views.home,name="home"),
]