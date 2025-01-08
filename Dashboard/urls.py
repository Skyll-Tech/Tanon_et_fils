from django.contrib import admin
from django.urls import path
from Dashboard import views

urlpatterns = [
    path("test", views.test, name="test"),
    path("dashboard", views.dashboard, name = "dashboard"),
]
