#!/usr/bin/env python
# -*- coding:utf-8 -*-


from django.shortcuts import render, HttpResponse
import time
import json
from api.lichen.get_students import get_students


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

def get_students_list(request):
    data = get_students()
    if request.method == "POST":
        ans = {
            "code": "ok",
            "data": data
        }
    return HttpResponse(json.dumps(ans))