from django.shortcuts import render, redirect, HttpResponse
import json
from . import models


# 测试注册界面
# http://0.0.0.0:8800/database/register
def register(request):
    if request.method == "POST":
        ans = {
            'user_name': request.POST.get("user"),
            'passwd': request.POST.get("passwd"),
            'gender': request.POST.get("gender"),
            'group': request.POST.get("group")
        }
        user = models.User(name=ans['user_name'],
                           passwd=ans['passwd'],
                           gender=ans['gender'],
                           group=ans['group'],
                           )
        user.save()
        return HttpResponse("%s<br><br>%s" % (json.dumps(ans, ensure_ascii=False), "<a href=\"../database/register\">返回</a>"))
    return render(request, "database/register.html", {})


"""
from TestModel.models import Test
# 数据库操作
def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
"""


# 测试添加班级
# http://0.0.0.0:8800/database/add_class
def add_class(request):
    if request.method == "POST":
        ans = {
            'name': request.POST.get("name"),
            'room': request.POST.get("room"),
        }
        o_class = models.Class(name=ans['name'],
                               room=ans['room'],
                               )
        o_class.save()
        return HttpResponse("%s<br><br>%s" % (json.dumps(ans, ensure_ascii=False),
                                              "<a href=\"../database/add_class\">返回</a>"))
    return render(request, "database/add_class.html", {})


# 测试添加可选项目
# http://0.0.0.0:8800/database/add_project
def add_project(request):
    if request.method == "POST":
        ans = {
            'name': request.POST.get("name"),
            'content': request.POST.get("content"),
        }
        project = models.ProjectPool(name=ans['name'],
                                     content=ans['content'],
                                     )
        project.save()
        return HttpResponse("%s<br><br>%s" % (json.dumps(ans, ensure_ascii=False),
                                              "<a href=\"../database/add_project\">返回</a>"))
    return render(request, "database/add_project.html", {})


# 测试添加可选项目
# http://0.0.0.0:8800/database/add_stage
def add_stage(request):
    if request.method == "POST":
        ans = {
            'name': request.POST.get("name"),
            'tid': int(request.POST.get("tid")),
        }
        print(ans)
        stage = models.Stage(
            name=ans['name'],
            teacher_id=ans['tid'],
        )
        stage.save()
        return HttpResponse("%s<br><br>%s" % (json.dumps(ans, ensure_ascii=False),
                                              "<a href=\"../database/add_stage\">返回</a>"))
    # 获取教师列表
    teacher_list = models.User.objects.filter(group='T')
    # print(list(teacher_list))
    m = {'teacher_list':[]}
    for i in teacher_list:
        print(i.id, i.name)
        m['teacher_list'].append({'id': i.id, 'name': i.name})

    return render(request, "database/add_stage.html", m)
