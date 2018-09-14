from django.contrib import admin
from django.urls import path, include, re_path
from addProject import views

urlpatterns = [
    re_path(r'^$', views.addProject, name='Add Project')
    ]