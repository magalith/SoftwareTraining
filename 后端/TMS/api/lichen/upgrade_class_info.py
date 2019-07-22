from database.models import User, Class

# 管理员接口，更新班级信息
def upgrade_class(dir_post):

    new_class_id = []
    for i in dir_post:
        # 实例化temp_class，用于写入数据库
        temp_class = Class()
        # 更新class.name  class.room
        temp_class.name = i['class_name']
        temp_class.room = i['room']
        temp_id = temp_class.id
        temp_class.save()
        new_class_id.append(str(temp_class.id))
        # new_class_id = ["C001","C002", "C003"]

        # 更新老师班级id
        teacher = User.objects.filter(name=i['teacher'])[0]
        teacher.class_id = temp_id


        # 更新学生班级id
        for j in i['students']:
            student = User.objects.filter(id=int(j))[0]
            student.class_id = temp_id

    return new_class_id




