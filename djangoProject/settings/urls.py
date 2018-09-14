from django.contrib import admin
from django.urls import path, include, re_path
from settings import views

urlpatterns = [
    re_path(r'^$', views.settings, name='Settings')
    ]