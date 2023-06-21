#-*- coding:utf-8 -*-

from django.urls import path, re_path
from . import views

# namespace

urlpatterns = [
    path('create/', views.ApartamentCreateView.as_view(), name='apartament_create'),
    # Retrieve apartament list
    path('', views.ApartamentListView.as_view(), name='apartament_list'),
    # Retrieve single apartament object
    re_path(r'^(?P<pk>\d+)/$', views.ApartamentDetailView.as_view(), name='apartament_detail'),
    # Update a apartament
    re_path(r'^(?P<pk>\d+)/update/$', views.ApartamentUpdateView.as_view(), name='apartament_update'),
    # Delete a apartament
    re_path(r'^(?P<pk>\d+)/delete/$', views.ApartamentDeleteView.as_view(), name='apartament_delete')

    # # Create a apartament
    # path('create/', views.apartament_create, name='apartament_create'),
    # # Retrieve apartament list
    # path('', views.apartament_list, name='apartament_list'),
    # # Retrieve single apartament object
    # re_path(r'^(?P<pk>\d+)/$', views.apartament_detail, name='apartament_detail'),
    # # Update a apartament
    # re_path(r'^(?P<pk>\d+)/update/$', views.apartament_update, name='apartament_update'),
    # # Delete a apartament
    # re_path(r'^(?P<pk>\d+)/delete/$', views.apartament_delete, name='apartament_delete'),

]