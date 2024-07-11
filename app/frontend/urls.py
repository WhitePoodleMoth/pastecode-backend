from django.contrib import admin
from django.urls import path
from frontend.views import search

urlpatterns = [
    path('<str:slug>', search),
]
