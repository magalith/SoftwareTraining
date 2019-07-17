#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render, HttpResponse
import json


# 测试界面,用于测试接口是否正常以及网络是否通畅
def test(request):
    ans = {
        "code": "ok",
        "data": "Success!",
    }
    return HttpResponse(json.dumps(ans))
