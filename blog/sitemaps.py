from django.contrib.sitemaps import Sitemap
from .models import Post
from django.urls import reverse

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.date_posted

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return ['newsapp:news_home', 'blog:blog-home', 'blog:blog-about', 'blog:blog-contact', 'blog:services', 'newsapp:bbc', 'newsapp:wsj', 'newsapp:corona']

    def location(self, item):
        return reverse(item)
