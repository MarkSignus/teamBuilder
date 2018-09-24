from django.contrib import admin
from django.urls import path, include, re_path
from settings import views

from settings.views import LocationListView, ClientListView, PartnerListView, SkillListView, WeekListView


urlpatterns = [
    re_path(r'^$', views.settings, name='Settings'),
    re_path('locations', LocationListView.as_view()),
    re_path('clients', ClientListView.as_view()),
    re_path('partners', PartnerListView.as_view()),
    re_path('skills', SkillListView.as_view()),
    re_path('weeks', WeekListView.as_view())
    
    ]



