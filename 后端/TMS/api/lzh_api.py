#!/usr/bin/env python
# -*- coding:utf-8 -*-


from django.shortcuts import render, redirect, HttpResponse
from database import models
import json
import os


# 获取所有文档信息
def get_all_doc():
    ans = {
        "code": "ok",
        "data": []
    }
    docs = models.Doc.objects.all()
    for doc in docs:
        temp = {
            "id": doc.id,
            "text": doc.text,
            "file": doc.file,
            "score": doc.score,
        }
        ans['data'].append(temp)
    return ans
