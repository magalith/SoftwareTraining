from django.shortcuts import render, redirect, HttpResponse
import json
from . import models
from tools.OSS import upload_to_bucket


# 跳转界面
def index(request):
    return render(request, "database/index.html", {})


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

        teacher = models.User.objects.filter(id=ans['tid'])[0]
        stage = models.Stage(
            name=ans['name'],
            teacher_id=teacher,
        )
        # stage.teacher_id.add(teacher)
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


# 测试为阶段添加任务
# http://0.0.0.0:8800/database/add_mission
def add_mission(request):
    if request.method == "POST":
        ans = {
            'text': request.POST.get("text"),
            'file': request.FILES.get('file'),
            # 'uid': int(request.POST.get("uid")),
            'sid': int(request.POST.get("sid")),
            'endtime': int(request.POST.get("endtime")),
        }
        file_url = upload_to_bucket(ans['file'])
        ans['file'] = file_url
        stage = models.Stage.objects.filter(id=ans['sid'])[0]
        doc = models.Doc(
            text=ans['text'],
            file=ans['file'],
            user_id=stage.teacher_id
        )
        doc.save()
        print("已经添加文稿")
        pass
        mission = models.Mission(
            doc_id=doc,
            stage_id=models.Stage.objects.filter(id=ans['sid'])[0],
            deadline=ans['endtime']
        )
        mission.save()

        # 更新文档从属的mission_id
        doc.mission_id = mission
        doc.save()
        return HttpResponse("%s<br><br>%s" % (json.dumps(ans, ensure_ascii=False),
                                              "<a href=\"../database/add_mission\">返回</a>"))
    ######################################################################################
    # GET 方法
    # 获取用户列表
    teacher_list = models.User.objects.filter(group='T')
    m = {'teacher_list': [], 'stage_list': []}
    for i in teacher_list:
        print(i.id, i.name)
        m['teacher_list'].append({'id': i.id, 'name': i.name})

    stage_list = models.Stage.objects.all()
    for j in stage_list:
        t_name = j.teacher_id.name
        m['stage_list'].append({'id': j.id, 'name': str(t_name + ' ' + j.name)})
    return render(request, "database/add_mission.html", m)


# 测试为阶段添加文档
# http://0.0.0.0:8800/database/add_doc
def add_doc(request):
    if request.method == "POST":
        ans = {
            'text': request.POST.get("text"),
            'file': request.FILES.get('file'),
            'uid': int(request.POST.get("uid")),
            'mid': int(request.POST.get("mid")),
        }
        file_url = upload_to_bucket(ans['file']) if ans['file'] else ""
        ans['file'] = file_url
        print(ans)

        upload_user = models.User.objects.filter(id=ans['uid'])[0]
        if ans['mid']:
            choice_mission = models.Mission.objects.filter(id=ans['mid'])[0]
            # 该语句未经过测试!
            print("执行未经过测试的语句!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            doc = models.Doc(text=ans['text'], file=ans['file'], user_id=upload_user, mission_id=choice_mission)
        else:
            doc = models.Doc(text=ans['text'], file=ans['file'], user_id=upload_user)
        doc.save()

        return HttpResponse("%s<br><br>%s" % (json.dumps(ans, ensure_ascii=False),
                                              "<a href=\"../database/add_doc\">返回</a>"))

    ######################################################################################
    # GET 方法
    # 获取任务列表
    mission_list = models.Mission.objects.all()

    m = {'mission_list': [], 'user_list': []}
    for i in mission_list:
        temp = models.Doc.objects.filter(id=i.doc_id.id)[0]
        print(i.id, temp.text)
        m['mission_list'].append({'id': i.id, 'name': i.doc_id.text})

    user_list = models.User.objects.all()
    for j in user_list:
        # print(j.id, j.name)
        m['user_list'].append({'id': j.id, 'name': j.name})

    return render(request, "database/add_doc.html", m)
