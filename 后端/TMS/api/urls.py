#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.urls import path, re_path
from . import views

urlpatterns = [
    #############
    #  通用接口  #
    #############
    # 测试界面,用于测试服务是否可用
    re_path("test/?", views.test),
    # 查看自己的信息
    re_path("get_self_info/?", views.test),

    ############
    # 管理员接口 #
    ############
    # 管理员查看全部学生名单
    re_path("get_students/?", views.test),
    # 管理员更新班级信息
    re_path("set_classes/?", views.test),
    # 管理员获取教师名单
    re_path("get_teachers/?", views.test),
    # 管理员获取所有班级名单(带学生老师名单)
    re_path("get_class_info/?", views.test),

    #############
    #  教师接口  #
    #############
    # 查看负责班级的学生名单
    # re_path("get_classinfo/?", views.test),
    # 查看所有阶段
    re_path("get_stage/?", views.test),
    # 为阶段添加任务
    re_path("push_mission/?", views.test),
    # 查看某一任务的所有文档
    re_path("check_mission/?", views.test),
    # 更新文档(学生的作业)分数
    re_path("set_score/?", views.test),
    # 获取某一个学生的所有文档(作业)信息
    re_path("get_students_doc/?", views.test),

    #############
    #  学生接口  #
    #############
    # 查看所有可选项目
    re_path("get_project_pool/?", views.test),
    # 更新学生选择的项目
    re_path("set_studentproj/?", views.test),
    # 查看所有的任务(包含已完成任务与未完成任务)
    re_path("get_missions/?", views.test),
    # 为某个任务提交文档(仅包含附件,文字留空)
    re_path("push_doc/?", views.test),
    # 获取所有的文档信息(包含得分)
    re_path("get_docs/?", views.test),
]
