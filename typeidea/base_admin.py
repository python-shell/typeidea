#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/19 15:40
# @Author  : jacson
# @FileName: base_admin.py
from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(owner=request.user)

