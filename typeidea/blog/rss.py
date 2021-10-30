#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/27 21:45
# @Author  : jacson
# @FileName: rss.py

from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.feedgenerator import Rss201rev2Feed
from .models import Post


class ExtendedFeed(Rss201rev2Feed):
    def add_item_elements(self, handler, item):
        super().add_item_elements(handler, item)
        handler.addQuickElement("content_html", item['content_html'])


class LatestPostFeed(Feed):
    feed_type = ExtendedFeed
    title = "Typeidea blog system"
    link = "/rss/"
    description = "Typeidea blog system powed by django"

    def items(self):
        return Post.objects.filter(status=Post.STATUS_NORMAL)[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.desc

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])

    def item_extra_kwargs(self, item):
        return {'content_html': self.item_content_html(item)}

    def item_content_html(self, item):
        return item.content_html