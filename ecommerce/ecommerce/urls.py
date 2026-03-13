from django.contrib import admin
from django.urls import path, include
from . import views
from eapp import views as eapp_views
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('eapp/', include('eapp.urls')),

    # Page list + single page
    path('page/', eapp_views.eapp_list, name='pages_list'),  # optional: shows all posts
    path('page/<slug:slug>/', eapp_views.eapp_pages, name='pages')  # single post
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)              