#!/usr/bin/env python
# -*- coding:utf-8 -*-


from django.shortcuts import render, redirect, HttpResponse
from database import models


# 主视图
def index(request):
    return render(request, "index.html", {})


# 登陆视图
def login(request):
    # POST方法
    if request.method == 'POST':
        login_info = {
            # user_name表示编号
            "username": request.POST.get("user_name"),
            "password": request.POST.get("password"),
            "timestamp": request.POST.get("timestamp"),
        }
        # 获取用户ID
        user = models.User.objects.filter(id=login_info['username'])
        if login_info['password'] == user.passwd:
            request.session["id"] = user.id
            request.session["name"] = user.name
            request.session["gender"] = user.gender
            request.session["group"] = user.group
        else:
            # 用户名错误,需要重新输入
            return redirect("/login/")
        views = {
            "R": redirect("/admin_student/"),
            "T": redirect("//"),
            "S": redirect("//"),
        }
        return views[request.session.get("group")]
    # GET方法,返回登录渲染界面
    return render(request, "login.html", {})


#
def admin_teacher(request):
    return render(request, "admin_teacher.html", {})


def class_page(request):
    return render(request, "admin_Class_Page.html", {})


def admin_student(request):
    return render(request, 'admin_student.html', {})
