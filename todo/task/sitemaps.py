
from django.contrib.sitemaps import Sitemap
from .models import Task

class TaskSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Task.objects.all()
