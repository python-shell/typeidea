#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/19 11:44
# @Author  : jacson
# @FileName: custom_site.py
from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = 'Typeidea管理后台'

    # Text to put in each page's <h1>.
    site_header = 'Typeidea'

    # Text to put at the top of the admin index page.
    index_title = '首页'
    site_url = '/aaa'


custom_site = CustomSite(name='cus_admin')

