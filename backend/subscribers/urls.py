from django.contrib import admin
from django.urls import path, include
from .views import SubscriberView

urlpatterns = [
    path('',SubscriberView.as_view(), name='SubscriberView'),
]

