#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/25 11:29
# @Author  : jacson
# @FileName: forms.py
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    def clear_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError("内容长度太短！！")
        return content

    class Meta:
        model = Comment
        fields = ['nickname', 'email', 'website', 'content']
