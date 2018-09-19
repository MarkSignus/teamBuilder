from django.contrib import admin
from django.urls import path, include, re_path
from associates import views
from associates.views import AssociateListView
from associates.views import assoc_partner_relationship_List,assoc_client_relationship_List,assoc_skill_List

urlpatterns = [
        re_path(r'^$', AssociateListView.as_view()),
        re_path('assoc_partner',assoc_partner_relationship_List.as_view()),
        re_path('assoc_client',assoc_client_relationship_List.as_view()),
        re_path('assoc_skill',assoc_skill_List.as_view())
    ]