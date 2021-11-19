from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('test/', views.test),
    path('api/videos/', views.VideoDataViews.as_view()),
    path('videos/', views.fetchData, name='videos'),
    path('api/search/', views.SearchVideos.as_view()),
]
