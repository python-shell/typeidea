#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/19 9:48
# @Author  : jacson
# @FileName: adminforms.py
from django import forms
from ckeditor.widgets import CKEditorWidget


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label="摘要", required=False)
    content = forms.CharField(widget=CKEditorWidget, label="正文", required=True)