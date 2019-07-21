from database.models import User

# 管理员接口，查看全部学生名单
def get_teachers():

    # 获取老师列表
    teachers_list = User.objects.filter(group='T')
    values = {'teachers_list': []}
    for i in teachers_list:
        # temp_class = Class.objects.filter(id=i.class_id.id)[0]
        if (i.class_id is None):
            values['teachers_list'].append({'id': i.id,
                                            'name': i.name,
                                            'class': "NULL"
                                            })
        else:
            values['teachers_list'].append({'id': i.id,
                                            'name': i.name,
                                            'class': i.class_id.name
                                            })
    return values