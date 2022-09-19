from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('/', views.post_subscriber, name='post_subscriber'),
]