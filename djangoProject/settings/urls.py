from django.contrib import admin
from django.urls import path, include, re_path
from settings import views

from settings.views import LocationListView
from settings.views import ClientListView
from settings.views import PartnerListView
from settings.views import SkillListView


urlpatterns = [
    re_path(r'^$', views.settings, name='Settings'),
    re_path('locations', LocationListView.as_view()),
    re_path('clients', ClientListView.as_view()),
    re_path('partners', PartnerListView.as_view()),
    re_path('skills', SkillListView.as_view()),
    ]



