from django.urls import path
from . import views

urlpatterns = [
    path('', views.eapp_list, name='list'),              # /page/ shows all posts
    path('<slug:slug>/', views.eapp_pages, name='pages'), # /page/<slug>/ shows single post
]