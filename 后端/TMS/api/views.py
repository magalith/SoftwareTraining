#!/usr/bin/env python
# -*- coding:utf-8 -*-


from django.shortcuts import render, redirect, HttpResponse
from api.lichen.get_students import get_students
from api.lichen.get_teachers import get_teachers
from api.lichen.upgrade_class_info import upgrade_class
from api.lichen.get_class_info import class_info
from api.lichen.upgrade_member_info import upgrade_member_informa
from tools import SMS
from . import lzh_api
import time
import json


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
########################       @Licunhao       ############################
###########################################################################



# 管理员获取所有学生列表
def get_students_list(request):
    if request.method == "POST":
        try:
            group = request.session.get("group") # group
            if not group:
                return HttpResponse(json.dumps(lzh_api.error_with_code(1001), ensure_ascii=False))
            elif(group == "S"):
                # 学生权限请求，返回权限错误
                return HttpResponse(json.dumps(lzh_api.error_with_code(1002), ensure_ascii=False))
            else:
                data = get_students()
                ans = {"code": "ok","data": data['students_list']}
                # 正确的返回结果
                return HttpResponse(json.dumps(ans, ensure_ascii=False))
        except Exception as e:
            # 若执行过程报错,则返回通用错误.
            print(e)
            return HttpResponse(json.dumps(lzh_api.error_with_code(0), ensure_ascii=False))
    else:
        # GET方法请求本接口,服务拒绝.
        return HttpResponse(json.dumps(lzh_api.error_with_code(2004), ensure_ascii=False))


# 管理员更新班级列表
def upgrade_class_info(request):
    if request.method == "POST":
        try:
            group = request.session.get("group") # group
            if not group:
                return HttpResponse(json.dumps(lzh_api.error_with_code(1001), ensure_ascii=False))
            elif(group == "T" or group == "S"):
                return HttpResponse(json.dumps(lzh_api.error_with_code(1002), ensure_ascii=False))
            else:
                dir_post =json.loads(request.POST.get("class"))
                re_data = upgrade_class(dir_post[0])
                ans = {"code": "ok","data": re_data}
                # 正确的返回结果
                return HttpResponse(json.dumps(ans, ensure_ascii=False))
        except Exception as e:
            # 若执行过程报错,则返回通用错误.
            print(e)
            return HttpResponse(json.dumps(lzh_api.error_with_code(0), ensure_ascii=False))
    else:
        # GET方法请求本接口,服务拒绝.
        return HttpResponse(json.dumps(lzh_api.error_with_code(2004), ensure_ascii=False))


# 管理员获取所有老师列表
def get_teachers_list(request):
    if request.method == "POST":
        try:
            group = request.session.get("group") # group
            if not group:
                return HttpResponse(json.dumps(lzh_api.error_with_code(1001), ensure_ascii=False))
            elif(group == "T" or group == "S"):
                return HttpResponse(json.dumps(lzh_api.error_with_code(1002), ensure_ascii=False))
            else:
                data = get_teachers()
                ans = {"code": "ok","data": data['teachers_list']}
                # 正确的返回结果
                return HttpResponse(json.dumps(ans, ensure_ascii=False))
        except Exception as e:
            # 若执行过程报错,则返回通用错误.
            print(e)
            return HttpResponse(json.dumps(lzh_api.error_with_code(0), ensure_ascii=False))
    else:
        # GET方法请求本接口,服务拒绝.
        return HttpResponse(json.dumps(lzh_api.error_with_code(2004), ensure_ascii=False))


# 获取所有班级信息
def get_class_info(request):
    if request.method == "POST":
        try:
            group = request.session.get("group") # group
            if not group:
                return HttpResponse(json.dumps(lzh_api.error_with_code(1001), ensure_ascii=False))
            elif(group == "T" or group == "S"):
                return HttpResponse(json.dumps(lzh_api.error_with_code(1002), ensure_ascii=False))
            else:
                data = class_info()
                ans = {"code": "ok", "data": data}
                # 正确的返回结果
                return HttpResponse(json.dumps(ans, ensure_ascii=False))
        except Exception as e:
            # 若执行过程报错,则返回通用错误.
            print(e)
            return HttpResponse(json.dumps(lzh_api.error_with_code(0), ensure_ascii=False))
    else:
        # GET方法请求本接口,服务拒绝.
        return HttpResponse(json.dumps(lzh_api.error_with_code(2004), ensure_ascii=False))

# 管理员更新已有班级成员信息
def upgrade_member_info(request):
    if request.method == "POST":
        try:
            group = request.session.get("group") # group
            if not group:
                return HttpResponse(json.dumps(lzh_api.error_with_code(1001), ensure_ascii=False))
            elif group == "S":
                return HttpResponse(json.dumps(lzh_api.error_with_code(1002), ensure_ascii=False))
            else:
                dir_post = json.loads(request.POST.get("class"))["class"]
                print(dir_post[0])
                judge = upgrade_member_informa(dir_post[0])
                if judge == False:
                    return HttpResponse(json.dumps(lzh_api.error_with_code(2001), ensure_ascii=False))
                elif judge == True:
                    ans = {"code": "ok"}
                    # 正确的返回结果
                    return HttpResponse(json.dumps(ans, ensure_ascii=False))
        except Exception as e:
            # 若执行过程报错,则返回通用错误.
            print(e)
            return HttpResponse(json.dumps(lzh_api.error_with_code(0), ensure_ascii=False))
    else:
        # GET方法请求本接口,服务拒绝.
        return HttpResponse(json.dumps(lzh_api.error_with_code(2004), ensure_ascii=False))






###########################################################################
########################     @Lizhenghao       ############################
########################       Data API        ############################
########################  2019-07-20 20:20:04  ############################
###########################################################################


# 获取所有文档api
def get_docs(request):
    if request.method == "POST":
        try:
            uid = request.session.get("uid") # group
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


# 教师查看某一学生提交的所有文档
def get_all_student_docs(request):
    timestamp = request.POST.get("timestamp")
    sid = int(request.POST.get("s_id"))
    ans = lzh_api.get_all_doc_of_student(sid)
    return HttpResponse(json.dumps(ans, ensure_ascii=False))


# 2.5 教师更新学生作业(文档)分数
# TODO 该接口未经过测试,需要在后续版本中进行测试
def update_student_docs(request):
    timestamp = request.POST.get("timestamp")
    # 学生文档列表
    score_list = json.loads(request.POST.get("score"))
    ans = lzh_api.update_doc_score(score_list=score_list)
    return HttpResponse(json.dumps(ans, ensure_ascii=False))


# 2.4 教师查看某一任务的所有文档
def check_missions_docs(request):
    timestamp = request.POST.get("timestamp")
    # 学生文档列表
    mid = int(request.POST.get("mission_id"))
    ans = lzh_api.check_all_mission_doc(mid=mid)
    return HttpResponse(json.dumps(ans, ensure_ascii=False))


# 2.3 教师为自己的阶段添加任务
# TODO 该方法未经过验证,需要经过前端测试才能够稳定使用
def add_mission(request):
    timestamp = request.POST.get("timestamp")
    # 学生文档列表
    sid = int(request.POST.get("stage_id"))
    mission_data = json.loads(request.POST.get("mission"))
    ans = lzh_api.add_mission_in_stage(uid=int(request.session.get("uid")), stage_id=sid, missions_data=mission_data)
    return HttpResponse(json.dumps(ans, ensure_ascii=False))


# 2.2 教师查看自己负责的所有阶段
def get_all_self_stage(request):
    timestamp = request.POST.get("timestamp")
    # 学生文档列表
    uid = int(request.session.get("uid"))
    ans = lzh_api.teacher_check_all_stage(uid=uid)
    return HttpResponse(json.dumps(ans, ensure_ascii=False))


# 通用接口 用户查看自己的信息
def get_self_information(request):
    timestamp = request.POST.get("timestamp")
    # 学生文档列表
    uid = int(request.session.get("uid"))
    ans = lzh_api.get_self_information(uid=uid)
    return HttpResponse(json.dumps(ans, ensure_ascii=False))


# 通用接口 获取所有项目
def get_all_user_project(request):
    timestamp = request.POST.get("timestamp")
    # 学生文档列表
    ans = lzh_api.get_all_projects()
    return HttpResponse(json.dumps(ans, ensure_ascii=False))


# 管理员接口 更新用户名单
def operate_user_info(request):
    timestamp = request.POST.get("timestamp")
    # 用户操作方法
    method = request.POST.get("method")
    # 用户列表
    user_list = json.loads(request.POST.get("user_list"))
    ans = lzh_api.operate_student_list(method=str(method).lower(), user_list=user_list)
    return HttpResponse(json.dumps(ans, ensure_ascii=False))


# 发送短信接口
def send_sms(request):
    phone_number = request.POST.get("phone")
    ans = lzh_api.get_verification_code_for_phone(phone_number=phone_number, method="L")
    return HttpResponse(json.dumps(ans, ensure_ascii=False))


# 使用手机号+验证码登陆
def phone_login(request):
    phone_number = request.POST.get("phone")
    v_code = request.POST.get("code")
    ans = lzh_api.login_with_verification_code(phone_number=str(phone_number), code=str(v_code))
    if ans.get("code") == "ok":
        # 登陆成功,跳转到登陆界面
        views = {
            "R": "/admin_student/",
            "T": "/tch_add_task/",
            "S": "/stu_select_pro/",
        }
        session_info = ans.get("data")
        request.session["uid"] = session_info.get("uid")
        request.session["name"] = session_info.get("name")
        request.session["gender"] = session_info.get("gender")
        request.session["group"] = session_info.get("group")
        return HttpResponse(views[request.session.get("group")])
    return HttpResponse("/login?view=phone&type=error")


# 操作班级信息(添加或删除)
def operate_class_info(request):
    method = request.POST.get("method")
    class_json = request.POST.get("class")
    class_list = json.loads(class_json) if class_json else []
    ans = lzh_api.operate_class_with_method(method=method, class_list=class_list)
    return HttpResponse(json.dumps(ans, ensure_ascii=False))
