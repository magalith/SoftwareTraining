from database.models import User, Class

# 管理员接口，查看全部学生名单
def class_info():

    # 获取老师列表
    class_list = Class.objects.all()
    classes_list = []
    for i in class_list:
        # temp_class = Class.objects.filter(id=i.class_id.id)[0]
        # 查询同一班级的学生与学生id
        classes_list.append({"cid":i.information()["id"],"name": i.information()["name"],"teacher_id": i.information()["teachers"],"students_id": i.information()["students"]})
    return classes_list
