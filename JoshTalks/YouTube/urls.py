from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('videos/', views.youtube_search)
]