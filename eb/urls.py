from eb.views import *
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('controller', views.controller_view, name='controller')
]
