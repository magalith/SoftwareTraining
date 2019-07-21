from django.shortcuts import render, HttpResponse
import time
import json
from database.models import User, Class, ProjectPool



# 管理员接口，查看全部学生名单
def get_students():

    # 获取学生列表
    students_list = User.objects.filter(group='S')
    teachers_list = User.objects.filter(group='T')
    values = {'students_list': []}
    count = 0
    for i in students_list:
        temp_class = Class.objects.filter(id=i.class_id)[0]
        values['students_list'].append({'id': i.id,
                                        'stuname': i.name,
                                        'class': temp_class.name,
                                        'teacher': i.id,
                                        "note": ProjectPool.objects.filter(id=i.project_id)[0].name
                                        })
        for j in teachers_list:
            if(i.class_id == j.class_id):
                values['students_list'][count]['teacher'] = j.name
        count += 1

    return values