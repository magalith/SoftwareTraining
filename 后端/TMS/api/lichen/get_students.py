from database.models import User

# 管理员接口，查看全部学生名单
def get_students():

    # 获取学生列表
    students_list = User.objects.filter(group='S')
    teachers_list = User.objects.filter(group='T')
    values = {'students_list': []}
    count = 0
    for i in students_list:
        # temp_class = Class.objects.filter(id=i.class_id.id)[0]
        if (i.class_id is None):
            values['students_list'].append({'id': i.id,
                                            'stuname': i.name,
                                            'class': "NULL",#i.class_id.name,
                                            'teacher': True,
                                            "note": "" ,#i.project_id.name
                                            })
            if (i.project_id is None):
                values['students_list'].append({'id': i.id,
                                                'stuname': i.name,
                                                'class': "NULL",  # i.class_id.name,
                                                'teacher': True,
                                                "note": "NULL",  # i.project_id.name
                                                })
            else:
                values['students_list'].append({'id': i.id,
                                                'stuname': i.name,
                                                'class': "NULL",
                                                'teacher': True,
                                                "note": i.project_id.name,
                                                # ProjectPool.objects.filter(id=i.project_id.id)[0].name
                                                })
        else:
            values['students_list'].append({'id': i.id,
                                            'stuname': i.name,
                                            'class': i.class_id.name,
                                            'teacher': True,
                                            "note": i.project_id.name,
                                            # ProjectPool.objects.filter(id=i.project_id.id)[0].name
                                            })

        for j in teachers_list:
            if(i.class_id == j.class_id):
                values['students_list'][count]['teacher'] = j.name
        count += 1

    return values