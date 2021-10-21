#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/15 10:55
# @Author  : jacson
# @FileName: __init__.py.py

class Meta(type):
    pass
class Complex(metaclass=Meta):
    pass
class Complex2(Meta):
    pass
print(type(Complex))
print(Complex)
print(type(Complex2))
print(type(type))
print(Complex2)
print(type(Complex()))