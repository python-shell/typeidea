#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/27 22:12
# @Author  : jacson
# @FileName: sitemap.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Post


class BlogSitemap(Sitemap):
    changefreq = "always"
    priority = 1.0
    protocol = 'https'

    def items(self):
        return Post.objects.filter(status=Post.STATUS_NORMAL)

    def lastmod(self, obj):
        return obj.created_time

    def location(self, obj):
        return reverse('post_detail', args=[obj.id,])