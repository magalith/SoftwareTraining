#!/usr/bin/env python
# -*- coding:utf-8 -*-


from django.shortcuts import render, redirect, HttpResponse
from database import models
from tools import OSS, SMS
import datetime
import time
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
            2004: {"type": "网络错误", "detail": "错误的请求方法,该接口仅支持POST方法"},
            2005: {"type": "网络错误", "detail": "错误的请求方法,该接口仅支持GET方法"},
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


# 为已有的任务添加文档
def add_doc_for_mission(uid, mid, file, text=""):
    ans = {
        "code": "ok",
        "data": {}
    }
    file_url = OSS.upload_to_bucket(file)
    # 获取提交用户对象
    user = models.User.objects.filter(id=uid)[0]
    # 获取指定任务对象
    mission = models.Mission.objects.filter(id=mid)[0]
    # 新建的文稿对象
    doc = models.Doc(text=text, file=file_url, user_id=user, mission_id=mission)
    doc.save()
    ans["data"] = {
        "id": doc.id,
        "text": doc.text,
        "file": doc.file,
        "deadline": mission.deadline,
    }
    return ans


# 查看学生所属教师布置的所有任务,以及自己的完成情况
def get_all_mission_status(student_id):
    ans = {
        "code": "ok",
    }
    # 获取当前学生用户
    student = models.User.objects.filter(id=student_id, group="S")[0]
    # 获取学生的指导教师
    teacher = models.User.objects.filter(group="T", class_id=student.class_id)[0]
    # 获取教师的所有任务
    missions = []
    for m in models.Mission.objects.all():
        if m.doc_id.user_id.id == teacher.id:
            missions.append(m)
    # 将教师布置的任务信息放置在data列表中
    data = []
    for i in missions:
        temp = {
            "id": i.id,
            "text": i.doc_id.text,
            "file": i.doc_id.file,
            "deadline": i.deadline,
            "stage_id": i.stage_id.id,
            "stage_number": i.stage_id.stage_number,
        }
        data.append(temp)
    ans["data"] = data
    return ans


# 更新学生的项目
def update_student_project(sid, pid):
    ans = {
        "code": "ok",
    }
    student = models.User.objects.filter(id=sid, group="S")[0]
    project = models.ProjectPool.objects.filter(id=pid)[0]
    student.project_id = project
    student.save()
    data = {
        "project": {
            "id": project.id,
            "name": project.name,
            "detail": project.content,
        }
    }
    ans["data"] = data
    return ans


# 学生查看所有可选项目
def check_all_project():
    ans = {
        "code": "ok",
        "data": {},
    }
    project = models.ProjectPool.objects.all()
    data = []
    for i in project:
        temp = {
            "id": i.id,
            "name": i.name,
            "detail": i.content,
        }
        data.append(temp)
    ans["data"] = data
    return ans


# 教师获得某个学生的所有文档
def get_all_doc_of_student(sid):
    ans = {
        "code": "ok",
        "data": {},
    }
    student = models.User.objects.filter(id=sid, group="S")[0]
    docs = models.Doc.objects.filter(user_id=student)
    data = []
    for doc in docs:
        temp = {
            "id": doc.id,
            "text": doc.text,
            "file": doc.file,
            "score": doc.score,
        }
        data.append(temp)
    ans["data"] = data
    return ans


# 教师更新学生作业(文档)的分数
def update_doc_score(score_list):
    ans = {
        "code": "ok",
        "data": "Success",
    }
    # 文档对象列表
    doc_list = []
    try:
        for i in score_list:
            doc = models.Doc.objects.filter(id=int(i["did"]))[0]
            # 此处应当判断,分数是否在1~100之间
            doc.score = int(i["score"])
            doc_list.append(doc)
    except Exception as e:
        print("文档ID异常,数据库检索错误.错误: %s" % str(e))
        ans["code"] = 4001
        ans["data"] = "Fail"
    # 保存数据
    for doc in doc_list:
        doc.save()
    return ans


# 教师查看自己布置的某一任务的所有文档
def check_all_mission_doc(mid):
    ans = {
        "code": "ok",
        "data": {},
    }
    mission = models.Mission.objects.filter(id=int(mid))[0]
    all_doc = models.Doc.objects.all()
    doc_of_mission = []
    for doc in all_doc:
        if doc.mission_id is not None and doc.mission_id.id == mission.id and doc.id != mission.doc_id.id:
            doc_of_mission.append(doc)
    data = []
    for doc in doc_of_mission:
        temp = {
            "id": doc.id,
            "text": doc.text,
            "file": doc.file,
            "sid": doc.user_id.id,
            "score": doc.score,
        }
        data.append(temp)
    ans["data"] = data
    return ans


# 教师为属于自己的阶段添加任务
def add_mission_in_stage(uid, stage_id, missions_data):
    ans = {
        "code": "ok",
    }
    # 获取教师
    teacher = models.User.objects.filter(id=int(uid), group="T")[0]
    # 获取教师从属阶段
    stage = models.Stage.objects.filter(id=int(stage_id), teacher_id=teacher)[0]

    # 将文件上传至文件服务器
    file = missions_data["file"]
    file_url = OSS.upload_to_bucket(file) if file else ""
    missions_data["file"] = file_url
    m = missions_data
    # 新建文档
    doc = models.Doc(text=m["text"], file=m["file"])
    doc.save()
    deadline = int(m["deadline"])
    # 新建任务
    mission = models.Mission(doc_id=doc, stage_id=stage, deadline=deadline)
    mission.save()
    # 为文档关联任务
    doc.mission_id = mission
    doc.save()

    ans["data"] = mission.id
    return ans


# 教师查看自己负责的所有阶段
# TODO 未进行权限认证
def teacher_check_all_stage(uid):
    ans = {
        "code": "ok",
    }
    # 获取教师对象
    teacher = models.User.objects.filter(id=int(uid), group="T")[0]
    # 获取所有阶段
    stages = models.Stage.objects.filter(teacher_id=teacher)
    # stage数据列表
    data = []
    for stage in stages:
        temp = {
            "id": stage.id,
            "stage_number": stage.stage_number,
            "name": stage.name,
            "teacher_id": stage.teacher_id.id,
            "missions": [],
        }
        missions = models.Mission.objects.filter(stage_id=stage)
        missions_list = []
        for m in missions:
            temp_mission = {
                "id": m.id,
                "text": m.doc_id.text,
                "file": m.doc_id.file,
                "deadline": m.deadline,
                # "creat_time": m.create_time,
                # "creat_time": time.mktime(m.create_time.timetuple()),
                "creat_time": m.create_time.strftime("%Y-%m-%d"),
            }
            missions_list.append(temp_mission)
        temp["missions"] = missions_list
        data.append(temp)
    ans["data"] = data
    return ans


# 用户获取自己的信息
def get_self_information(uid):
    ans = {
        "code": "ok",
    }
    user = models.User.objects.filter(id=int(uid))[0]
    class_dic = {
        "id": user.class_id.id if user.class_id else 0,
        "name": user.class_id.name if user.class_id else "",
        "classroom": user.class_id.room if user.class_id else "",
    }
    project_dic = {
            "id": user.project_id.id if user.project_id else 0,
            "name": user.project_id.name if user.project_id else "",
            "content": user.project_id.content if user.project_id else "",
    }
    data = {
        "id": user.id,
        "name": user.name,
        "gender": {"M": "男性", "F": "女性", "U": "位置", }[user.gender],
        "class": class_dic,
        "group": {"R": "管理员", "T": "教师", "S": "学生", }[user.group],
        "project": project_dic,
        "score": 0,
    }
    ans["data"] = data
    return ans


# 获取所有可选项目
def get_all_projects():
    ans = {
        "code": "ok",
    }
    projects = models.ProjectPool.objects.all()
    data = []
    for proj in projects:
        temp = {
            "id": proj.id if proj else 0,
            "name": proj.name if proj else "",
            "content": proj.content if proj else "",
            "count": len(models.User.objects.filter(project_id=proj)),
        }
        data.append(temp)
    ans["data"] = data
    return ans


# 管理员管理学生名单
def operate_student_list(method, user_list):
    ans = {
        "code": "ok",
    }

    # 添加学生方法
    def add_user(ulist):
        out_data = "添加成功"
        for u in ulist:
            try:
                user = models.User(
                    name=u.get("name"),
                    passwd=u.get("password"),
                    gender=u.get("gender"),
                    group=u.get("group"),
                    phone=u.get("phone"),
                )
                user.save()
            except Exception as e:
                out_data = "添加失败\t" + str(e)
        return out_data

    # 删除学生方法
    def del_user(ulist):
        out_data = "删除成功"
        for uid in ulist:
            try:
                user = models.User.objects.get(id=int(uid))
                user.exist = False
                user.save()
            except Exception as e:
                out_data = "删除失败\t" + str(e)
        return out_data

    method_dic = {
        "add": add_user,
        "del": del_user,
    }
    operate = method_dic[str(method).lower()]
    data = operate(user_list)
    ans["data"] = data
    return ans


# 为手机号获取手机验证码
def get_verification_code_for_phone(phone_number, method):
    ans = {
        "code": "ok",
    }
    SMS_Info = SMS.sent_sms_with_phone(phone_number)
    code = SMS_Info["code"]
    v_code = models.VerificationCode(phone=str(phone_number), method=method, code=code)
    v_code.save()
    # 验证码三分钟后报废
    wast_time = v_code.create_time + datetime.timedelta(minutes=3)
    # 更新验证码作废时间
    v_code.waste_time = wast_time
    v_code.save()
    return ans
