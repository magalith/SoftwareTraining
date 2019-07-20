#!/usr/bin/env python
# -*- coding:utf-8 -*-


from django.shortcuts import render, HttpResponse
import time
import json
from . import lzh_api


# api版本视图
def api_index(requests):
    ans = {
        "code": "ok",
        "data": {
            "version": "V0.0.1",
            "Last Modified": "2019-07-18 21:52:59",
            "Current Time:": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        }
    }
    return HttpResponse(json.dumps(ans))


# 测试界面,用于测试接口是否正常以及网络是否通畅
def test(request):
    ans = {
        "code": "ok",
        "data": "Success!",
    }
    return HttpResponse(json.dumps(ans))


###########################################################################
########################     @Lizhenghao       ############################
########################       Data API        ############################
########################  2019-07-20 20:20:04  ############################
###########################################################################


# 获取所有文档api
def get_docs(request):
    if request.method == "POST":
        try:
            uid = request.session.get("uid")
            if not uid:
                return HttpResponse(json.dumps(lzh_api.error_with_code(1001), ensure_ascii=False))
            ans = lzh_api.get_all_doc(uid)
            # 正确的返回结果
            return HttpResponse(json.dumps(ans, ensure_ascii=False))
        except Exception as e:
            # 若执行过程报错,则返回通用错误.
            print(e)
            return HttpResponse(json.dumps(lzh_api.error_with_code(0), ensure_ascii=False))
    else:
        # GET方法请求本接口,服务拒绝.
        return HttpResponse(json.dumps(lzh_api.error_with_code(2004), ensure_ascii=False))


# 为指定任务提交文档
# TODO 未检查数据合法性
# 暂时未检查所属任务是否为指导老师所出,这个问题可能会造成数据泄露或不规范
# 若有时间,则需要对此问题进行修复
# TODO 非常紧急,返回值字段缺失
# 返回结果中,应当添加字段,表示自己提交的文稿信息.但是返回结果中没有包含该字段
def update_doc(request):
    if request.method == "POST":
        try:
            uid = request.session.get("uid")
            if not uid:
                return HttpResponse(json.dumps(lzh_api.error_with_code(1001), ensure_ascii=False))
            timestamp = int(request.POST.get("timestamp"))
            mid = int(request.POST.get("mission_id"))
            text = request.POST.get("text")
            file = request.FILES.get("file")
            ans = lzh_api.add_doc_for_mission(uid=uid, mid=mid, file=file, text=text)
            # 正确的返回结果
            return HttpResponse(json.dumps(ans, ensure_ascii=False))
        except Exception as e:
            # 若执行过程报错,则返回通用错误.
            print(e)
            return HttpResponse(json.dumps(lzh_api.error_with_code(0), ensure_ascii=False))
    else:
        # GET方法访问,拒绝请求.
        return HttpResponse(json.dumps(lzh_api.error_with_code(2004), ensure_ascii=False))


# 查看指导教师布置的所有任务信息
def get_all_mission(request):
    ans = lzh_api.get_all_mission_status(int(request.session.get("uid")))
    return HttpResponse(json.dumps(ans, ensure_ascii=False))


# 更新学生所选的项目信息
def update_student_project(request):
    timestamp = request.POST.get("timestamp")
    pid = int(request.POST.get("proj_id"))
    ans = lzh_api.update_student_project(int(request.session.get("uid")), pid)
    return HttpResponse(json.dumps(ans, ensure_ascii=False))


# 查看所有可选项目
def get_all_project(request):
    timestamp = request.POST.get("timestamp")
    ans = lzh_api.check_all_project()
    return HttpResponse(json.dumps(ans, ensure_ascii=False))
