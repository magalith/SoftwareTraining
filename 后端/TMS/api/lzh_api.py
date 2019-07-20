#!/usr/bin/env python
# -*- coding:utf-8 -*-


from django.shortcuts import render, redirect, HttpResponse
from database import models
import json
import os


# 错误消息
def error_with_code(code):
    ans = {
        "code": code,
    }
    try:
        data = {
            1001: {"type": "权限错误", "detail": "该接口需要登陆才能访问"},
            1002: {"type": "权限错误", "detail": "当前用户无权限访问指定内容"},
            1003: {"type": "权限错误", "detail": "错误的用户权限"},
            2001: {"type": "网络错误", "detail": "POST参数错误"},
            2002: {"type": "网络错误", "detail": "错误的数据格式"},
            2003: {"type": "网络错误", "detail": "附件超过指定大小"},
            3001: {"type": "会话错误", "detail": "会话已过期,或遭到中间人攻击"},
            3002: {"type": "会话错误", "detail": "会话异常,请重新登陆后尝试"},
            4001: {"type": "服务异常", "detail": "数据库访问异常"},
            4002: {"type": "服务异常", "detail": "服务器出现未知错误"},
            4003: {"type": "服务异常", "detail": "错误的查询结果"},
               0: {"type": "通用错误", "detail": "通用错误,表示该接口错误消息未完成"},
        }[code]
        ans["data"] = data
        return ans
    except Exception as e:
        return False


# 获取所有文档信息
def get_all_doc(uid):
    ans = {
        "code": "ok",
        "data": []
    }
    user = models.User.objects.filter(id=uid)[0]
    docs = models.Doc.objects.filter(user_id=user)
    for doc in docs:
        temp = {
            "id": doc.id,
            "text": doc.text,
            "file": doc.file,
            "score": doc.score,
        }
        ans['data'].append(temp)
    return ans
