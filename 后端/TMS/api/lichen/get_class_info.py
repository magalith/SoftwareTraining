from database.models import User, Class

# 管理员接口，查看全部学生名单
def class_info():

    # 获取老师列表
    class_list = Class.objects.all()
    stu_list = []
    tea_list = []
    values = {'class_list': []}
    for i in class_list:
        # temp_class = Class.objects.filter(id=i.class_id.id)[0]
        # 查询同一班级的学生与学生id
        user_id = User.objects.filter(class_id=i.id)
        if len(user_id) == True:
            for j in user_id:
                if j.group == 'S':
                # 判断是否为学生
                    stu_list.append(str(j.id))
                elif j.group == "T":
                # 判断是否为老师
                    tea_list.append(str(j.id))
                else:
                    pass

            values['class_list'].append({'cid': i.id,
                                    'name': i.name,
                                    'teacher_id': tea_list,
                                    'students_id': stu_list,})
    return values