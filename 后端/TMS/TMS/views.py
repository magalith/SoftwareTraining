#!/usr/bin/env python
# -*- coding:utf-8 -*-


from django.shortcuts import render, redirect, HttpResponse


# 主视图
def index(requests):
    return render(requests, "index.html", {})
