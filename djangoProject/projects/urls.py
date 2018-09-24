from django.contrib import admin
from django.urls import path, include, re_path
from projects.views import ProjectListView
from projects.views import proj_partner_relationship_List,proj_client_relationship_List,proj_skill_List,proj_assoc_List

urlpatterns = [
        re_path(r'^$', ProjectListView.as_view()),
        re_path('proj_associates/(?P<q>\w+)/',proj_assoc_List.as_view(),name ='proj_associates'),
        re_path('proj_skill/(?P<q>\w+)/',proj_skill_List.as_view(),name ='proj_skill'),
        re_path('proj_partner/(?P<q>\w+)/',proj_partner_relationship_List.as_view(),name ='proj_partner'),
        re_path('proj_client/(?P<q>\w+)/',proj_client_relationship_List.as_view(),name ='proj_client')
    ]