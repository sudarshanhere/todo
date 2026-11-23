
from django.contrib.sitemaps import Sitemap
from .models import task

class TaskSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return task.objects.all()
