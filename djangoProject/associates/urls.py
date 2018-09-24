from django.contrib import admin
from django.urls import path, include, re_path
from associates.views import AssociateListView
from associates.views import assoc_partner_relationship_List,assoc_client_relationship_List,assoc_skill_List,assoc_avail_List

urlpatterns = [
        re_path(r'^$', AssociateListView.as_view()),
        re_path('assoc_partner/(?P<q>\w+)/',assoc_partner_relationship_List.as_view(),name ='assoc_partner'),
        re_path('assoc_client/(?P<q>\w+)/',assoc_client_relationship_List.as_view(),name ='assoc_client'),
        re_path('assoc_skill/(?P<q>\w+)/',assoc_skill_List.as_view(),name ='assoc_skill'),
        re_path('assoc_availability/(?P<q>\w+)/',assoc_avail_List.as_view(),name ='assoc_availability')
    ]