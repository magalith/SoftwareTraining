#!/usr/bin/env python
# -*- coding:utf-8 -*-


from django.shortcuts import render, redirect, HttpResponse


# 主视图
def index(requests):
    return render(requests, "index.html", {})


# 登陆视图
def login(requests):
    return render(requests, "login.html", {})


#
def admin_teacher(requests):
    return render(requests, "admin_teacher.html", {})


def class_page(requests):
    return render(requests, "admin_Class_Page.html", {})


def admin_student(requests):
    return render(requests, 'admin_student.html', {})
