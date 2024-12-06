from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("home/", views.home),
]
