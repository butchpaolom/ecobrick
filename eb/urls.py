from eb.views import *
from eb.ajax_views import *
from django.urls import path
from . import views, ajax_views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.controller_view, name='settings'),
    #api
    path('api/settings', ajax_views.update_settings, name='update_settings'),
    path('api/get_settings/', ajax_views.get_settings, name='get_settings')
]

