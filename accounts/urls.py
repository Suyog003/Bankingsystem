from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from .models import customer,transactions

urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search, name="search"),
    path('transaction', views.transaction, name="transaction"),
    path('about', views.about, name="about"),
    path("user/<int:userid>/", views.userView, name="userView"),
]