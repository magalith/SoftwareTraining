#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.urls import path, re_path
from . import views

urlpatterns = [
    # 注册用户
    re_path(r"register/?", views.register),
    # 创建班级
    re_path(r"add_class/?", views.add_class),
    # 添加可选项目
    re_path(r"add_project/?", views.add_project),
    # 添加阶段
    re_path(r"add_stage/?", views.add_stage),
    # 添加任务
    re_path(r"add_mission/?", views.add_project),
    # 添加文稿
    re_path(r"add_doc/?", views.add_project),
]
