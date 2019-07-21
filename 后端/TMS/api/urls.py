#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.urls import path, re_path
from . import views


urlpatterns = [
    #############
    #  通用接口  #
    #############
    # api版本界面,用于测试服务是否可用
    path("", views.api_index),
    # 测试界面,用于测试服务是否可用
    re_path("test/?$", views.test),
    # 查看自己的信息
    re_path("get_self_info/?$", views.get_self_information),
    # 获取项目池中所有项目
    re_path("get_all_project/?$", views.get_all_user_project),
    # 发送短信
    re_path("send_sms/?$", views.send_sms),

    ############
    # 管理员接口 #
    ############
    # 管理员查看全部学生名单
    re_path("get_students/?$", views.get_students_list),
    # 管理员更新班级信息
    re_path("set_classes/?$", views.upgrade_class_info),
    # 管理员获取教师名单
    re_path("get_teachers/?$", views.get_teachers_list),
    # 管理员获取所有班级名单(带学生老师名单)
    re_path("get_class_info/?$", views.get_class_info),

    #############
    #  教师接口  #
    #############
    # 查看负责班级的学生名单
    # re_path("get_classinfo/?$", views.test),
    # 查看所有阶段
    re_path("get_stage/?$", views.get_all_self_stage),
    # 为阶段添加任务
    re_path("push_mission/?$", views.add_mission),
    # 查看某一任务的所有文档
    re_path("check_mission/?$", views.check_missions_docs),
    # 更新文档(学生的作业)分数
    re_path("set_score/?$", views.update_student_docs),
    # 获取某一个学生的所有文档(作业)信息
    re_path("get_students_doc/?$", views.get_all_student_docs),

    #############
    #  学生接口  #
    #############
    # 查看所有可选项目
    re_path("get_project_pool/?$", views.get_all_project),
    # 更新学生选择的项目
    re_path("set_studentproj/?$", views.update_student_project),
    # 查看所有的任务(包含已完成任务与未完成任务)
    re_path("get_missions/?$", views.get_all_mission),
    # 为某个任务提交文档(仅包含附件,文字留空)
    re_path("push_doc/?$", views.update_doc),
    # 获取所有的文档信息(包含得分)
    re_path("get_docs/?$", views.get_docs),
]
