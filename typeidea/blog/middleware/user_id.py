#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/26 17:45
# @Author  : jacson
# @FileName: user_id.py
import uuid

UID_KEY = 'uid'
TEN_YEARS = 60 * 60 * 24 * 365 * 10


class UserIDMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        uid = self.generated_uid(request)
        request.uid = uid
        response = self.get_response(request)
        response.set_cookie(UID_KEY, uid, max_age=TEN_YEARS, httponly=True)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def generated_uid(self, request):
        try:
            uid = request.COOKIES.get(UID_KEY)
        except KeyError:
            uid = uuid.uuid4().hex
        return uid
