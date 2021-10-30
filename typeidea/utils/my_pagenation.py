#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/29 18:38
# @Author  : jacson
# @FileName: my_pagenation.py
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 4
