
"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.sitemaps.views import sitemap

from task.sitemaps import TaskSitemap

sitemaps = {
    'tasks': TaskSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task.urls')),

    # Sitemap URL
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
]
