
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Task

class TaskSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Task.objects.all()

class PageSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ['home']  # Add your page names here

def location(self, item):
    from django.urls import reverse
    return reverse(item)
    