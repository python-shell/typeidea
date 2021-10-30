#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/29 15:00
# @Author  : jacson
# @FileName: serializers.py
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

from .models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'owner', 'created_time']


class CategoryDetailSerializer(CategorySerializer):
    posts = serializers.SerializerMethodField('paginated_posts')

    def paginated_posts(self, obj):
        posts = obj.post_set.filter(status=Post.STATUS_NORMAL)
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(posts, self.context['request'])
        serializer = PostSerializer(page, many=True, context={'request':
                                                              self.context['request']})
        return {
            'count': posts.count(),
            'results': serializer.data,
            'previous': paginator.get_previous_link(),
            'next': paginator.get_next_link()
        }

    class Meta:
        model = Category
        fields = ['id', 'name', 'owner', 'created_time', 'posts']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    tag = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    created_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Post
        fields = ['url', 'id', 'title', 'category', 'tag', 'desc', 'owner', 'created_time']
        extra_kwargs = {
            'url': {'view_name': 'api-post-detail'}
        }


class PostDetailSerializer(PostSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'tag', 'desc', 'owner', 'content_html', 'created_time']