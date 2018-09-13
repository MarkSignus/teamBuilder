from django.contrib import admin
from django.urls import path, include, re_path
from addUser import views

urlpatterns = [
    re_path(r'^$', views.addUser, name='Add User')
    ]