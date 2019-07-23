from database.models import User, Class

# 管理员接口，更新班级信息
def upgrade_member_info(dir_post):

    all_class = Class.objects.all()
    # get_class = Class.objects.filter(id=dir_post["class_id"])[0]
    temp = 0
    for each_class in all_class:
        if each_class.id == dir_post["class_id"]:
            temp = 1
        else:
            temp = 0

    if temp == 1:
        student = dir_post["student_id"]
        teacher = User.objects.filter(dir_post["teacher_id"])
        if (student is None) and (teacher is None):
                return False
        elif (student is None) and (teacher is not None):
            teacher[0].class_id.id = dir_post["class_id"]
            return True
        elif (student is not None) and (teacher is None):
            for j in dir_post["student_id"]:
                load_student = User.objects.filter(j)[0]
                load_student.class_id.id = dir_post["class_id"]
            return True
        else:
            teacher[0].class_id.id = dir_post["class_id"]
            for j in dir_post["student_id"]:
                load_student = User.objects.filter(j)[0]
                load_student.class_id.id = dir_post["class_id"]
            return True





