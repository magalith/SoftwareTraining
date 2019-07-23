#!/usr/bin/env python
# -*- coding:utf-8 -*-


from django.shortcuts import render, redirect, HttpResponse
from database import models


# 主视图
def index(request):
    return render(request, "index.html", {})


# 登陆视图
def login(request):
    # 不同权限登陆后跳转的url
    views = {
        "R": "/admin_student/",
        "T": "/tch_add_task/",
        "S": "/stu_select_pro/",
    }
    # POST方法
    if request.method == 'POST':
        login_info = {
            # user_name表示编号
            "username": int(request.POST.get("user_name")),
            "password": request.POST.get("password"),
            "timestamp": request.POST.get("timestamp"),
        }
        # 获取用户ID
        user = models.User.objects.filter(id=login_info['username'])[0]
        if login_info['password'] == user.passwd:
            # 触发用户Login方法
            user.login()
            request.session["uid"] = user.id
            request.session["name"] = user.name
            request.session["gender"] = user.gender
            request.session["group"] = user.group
        else:
            # 用户名错误,需要重新输入
            return redirect("/login/")
        return HttpResponse(views[request.session.get("group")])
    # GET方法,返回登录渲染界面
    group = request.session.get("group")
    if group:
        return redirect(views[group])
    return render(request, "login.html", {})


# 登出视图
def logout(request):
    request.session.flush()
    return redirect("/login")


#
def admin_teacher(request):
    if request.session.get("gropu") == "T":
        return render(request, "admin_teacher.html", {})


def class_page(request):
    return render(request, "admin_Class_Page.html", {})


def admin_student(request):
    return render(request, 'admin_student.html', {})


def doc_check(request):
    return render(request, 'student_score.html', {})


def select_project(request):
    return render(request, 'student_project.html', {})


def check_task(request):
    return render(request, 'student_checkTask.html', {})


def tch_add_task(request):
    return render(request, 'teacher_missionpage.html', {})


def tch_check_doc(request):
    return render(request, 'teacher_file_check.html', {})


def tch_check_stulist(request):
    return render(request, 'teacher_studentlist.html', {})


# 导入到重定向界面
def redirect_login(request):
    return render(request, "redirect_login.html", {})
