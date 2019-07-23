from database.models import User, Class

# 管理员接口，更新班级信息
def upgrade_member_informa(dir_post):
    out = True
    all_class = Class.objects.all()
    print()
    print(dir_post["teacher_id"], dir_post["students_id"])
    for each_class in all_class:
        temp = each_class.set_member(dir_post["teacher_id"], dir_post["students_id"])
        if temp == False:
            out = False
    return out








