from django.urls import path
from . import views

urlpatterns = [
      path('', views.eapp_list, name='eapp_list'),
   
]
