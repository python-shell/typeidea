#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/25 11:29
# @Author  : jacson
# @FileName: forms.py
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    nickname = forms.CharField(max_length=50, label='昵称', widget=forms.widgets.Input(
        attrs={'class': 'form-control', 'style': 'width: 60%'}
    ))
    email = forms.CharField(max_length=50, label='邮箱', widget=forms.widgets.Input(
        attrs={'class': 'form-control', 'style': 'width: 60%'}
    ))
    website = forms.CharField(max_length=50, label='网站', widget=forms.widgets.URLInput(
        attrs={'class': 'form-control', 'style': 'width: 60%'}
    ))
    content = forms.CharField(max_length=50, label='内容', widget=forms.widgets.Textarea(
        attrs={'class': 'form-control', 'style': 'width: 60%'}
    ))

    def clear_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError("内容长度太短！！")
        return content

    class Meta:
        model = Comment
        fields = ['nickname', 'email', 'website', 'content']
