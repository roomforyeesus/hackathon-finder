from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.SubscriberView.as_view(), name='SubscriberView'),
]