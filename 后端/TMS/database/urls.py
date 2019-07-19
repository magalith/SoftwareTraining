#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r"register/?", views.register),
]
