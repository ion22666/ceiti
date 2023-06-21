#-*- coding:utf-8 -*-

from django.urls import path, re_path
from . import views

# namespace
app_name = 'agent'

urlpatterns = [
    path('create/', views.AgentCreateView.as_view(), name='agent_create'),
    # Retrieve agent list
    path('', views.AgentListView.as_view(), name='agent_list'),
    # Retrieve single agent object
    re_path(r'^(?P<pk>\d+)/$', views.AgentDetailView.as_view(), name='agent_detail'),
    # Update a agent
    re_path(r'^(?P<pk>\d+)/update/$', views.AgentUpdateView.as_view(), name='agent_update'),
    # Delete a agent
    re_path(r'^(?P<pk>\d+)/delete/$', views.AgentDeleteView.as_view(), name='agent_delete')

    # # Create a agent
    # path('create/', views.agent_create, name='agent_create'),
    # # Retrieve agent list
    # path('', views.agent_list, name='agent_list'),
    # # Retrieve single agent object
    # re_path(r'^(?P<pk>\d+)/$', views.agent_detail, name='agent_detail'),
    # # Update a agent
    # re_path(r'^(?P<pk>\d+)/update/$', views.agent_update, name='agent_update'),
    # # Delete a agent
    # re_path(r'^(?P<pk>\d+)/delete/$', views.agent_delete, name='agent_delete'),

]