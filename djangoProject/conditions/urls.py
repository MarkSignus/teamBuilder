from django.contrib import admin
from django.urls import path, include, re_path
from conditions import views

urlpatterns = [
    re_path(r'^$', views.conditions, name='Conditions')
    ]