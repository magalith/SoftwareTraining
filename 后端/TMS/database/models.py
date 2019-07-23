#!/usr/bin/env python
# -*- coding:utf-8 -*-


from django.db import models
import datetime
import json


# 用户表
class User(models.Model):
    # 用户ID
    id = models.AutoField(primary_key=True)
    # 姓名,最长20个字
    name = models.CharField(max_length=20)
    # 用户加密密码,使用加盐SHA1值存储
    passwd = models.CharField(max_length=160)
    # 用户性别,采用单字母表示.F=女性;M=男性;U=未知
    gender = models.CharField(max_length=1, default='U')
    # 班级ID,为Class的外键.
    class_id = models.ForeignKey("Class", on_delete=models.SET_NULL, blank=True, null=True)
    # 用户选择项目ID
    project_id = models.ForeignKey("ProjectPool", on_delete=models.SET_NULL, blank=True, null=True)
    # 所属分组,R=管理员;T=教师;S=Student
    group = models.CharField(max_length=1, default='S')
    # 用户手机号,手机号只能被一个用户所绑定
    phone = models.CharField(max_length=15, blank=True, null=True, unique=True)
    # 判断记录是否存在
    exist = models.BooleanField(default=True)
    # 最后一次的登陆时间
    last_login_time = models.DateTimeField(auto_now_add=True)

    # Unicode字符串
    def __unicode__(self):
        return json.dumps(self.information())

    # 登录用户时,需要调用次函数,完成最后登陆时间、手机验证码清空等功能
    def login(self):
        # 重设最后登陆时间
        self.last_login_time = datetime.datetime.now()
        # 获取用户的所有未使用的手机登陆验证码记录
        code_records = VerificationCode.objects.filter(phone=str(self.phone), method="L", used=False)
        for code in code_records:
            # 将所有用户手机号登陆记录标记为已使用
            code.used = True
            code.save()
        return True

    # 获取字典格式的用户信息
    def information(self):
        info = {
            "id": self.id,
            "name": self.name,
            "gender": {
                "M": "男",
                "F": "女",
                "U": "未知",
            }[self.gender],
            "class": self.class_id.base_information() if self.class_id else {},
            "project": self.project_id.information() if self.project_id else {},
            "group": {
                "R": "管理员",
                "T": "教师",
                "S": "学生",
            }[self.group],
            "phone": self.phone,
            "last_login_time": self.last_login_time.strftime("%Y-%m-%d"),
        }
        return info


# 班级表
class Class(models.Model):
    # 班级id
    id = models.AutoField(primary_key=True)
    # 班级名称
    name = models.CharField(max_length=128)
    # 上课教室
    room = models.CharField(max_length=128)

    # Unicode字符串
    def __unicode__(self):
        return json.dumps(self.information())

    # 获取字典格式的班级信息
    def information(self):
        teachers = User.objects.filter(group="T", class_id=self)
        students = User.objects.filter(group="S", class_id=self)
        info = {
            "id": self.id,
            "name": self.name,
            "room": self.room,
            "teachers": [t.information() for t in teachers],
            "students": [s.information() for s in students],
        }
        return info

    # 获取简要的,字典格式的班级信息
    def base_information(self):
        info = {
            "id": self.id,
            "name": self.name,
            "room": self.room,
        }
        return info

    # 设置成员
    def set_member(self, teacher_list=[], student_list=[]):
        try:
            teachers = [User.objects.get(id=tid, group="T") for tid in teacher_list] if teacher_list else []
            students = [User.objects.get(id=sid, group="S") for sid in student_list] if student_list else []
            if self.clear_all_member() is False:
                raise Exception("清空班级成员错误")
        except:
            return False
        for t in teachers:
            t.class_id = self
            t.save()
        for s in students:
            s.class_id = self
            s.save()
        return True

    # 清空班级成员
    def clear_all_member(self):
        try:
            general_users = list(User.objects.filter(group="T")) + list(User.objects.filter(group="S"))
            for u in general_users:
                if u.class_id == self:
                    u.class_id = None
                    u.save()
            return True
        except:
            return False



# 可选项目池
class ProjectPool(models.Model):
    # 可选项目ID
    id = models.AutoField(primary_key=True)
    # 可选项目名称
    name = models.CharField(max_length=128)
    # 可选项目简介
    content = models.TextField(blank=True, null=True)

    # Unicode字符串
    def __unicode__(self):
        return json.dumps(self.information())

    # 获取字典格式的项目信息
    def information(self):
        users = User.objects.filter(project_id=self)
        info = {
            "id": self.id,
            "name": self.name,
            "content": self.content,
            "num_of_chooser": len(users),
        }
        return info


# 阶段表
class Stage(models.Model):
    # 阶段ID
    id = models.AutoField(primary_key=True)
    # 阶段名称
    name = models.CharField(max_length=128)
    # 阶段从属教师ID
    teacher_id = models.ForeignKey("User", on_delete=models.CASCADE)
    # 阶段编号,0,1,2号.该字段仅在初期开发时使用,若有时间,则会释放该字段
    stage_number = models.PositiveSmallIntegerField(default=0, blank=True, null=True)

    # Unicode字符串
    def __unicode__(self):
        return json.dumps(self.information())

    # 获取字典格式的阶段信息
    def information(self):
        info = {
            "id": self.id,
            "name": self.name,
            "teacher": self.teacher_id.information() if self.teacher_id else {},
            "number": self.stage_number,
        }
        return info


# 任务表
class Mission(models.Model):
    # 任务ID
    id = models.AutoField(primary_key=True)
    # 任务文档的ID,外键约束
    doc_id = models.ForeignKey("Doc", on_delete=models.CASCADE)
    # 阶段ID,外键约束
    stage_id = models.ForeignKey("Stage", on_delete=models.CASCADE)
    # 任务截止时间,整数时间戳
    deadline = models.PositiveIntegerField()
    # 任务创建时间,整数时间戳
    create_time = models.DateTimeField(auto_now_add=True)

    # Unicode字符串
    def __unicode__(self):
        return json.dumps(self.information())

    # 获取字典格式的任务信息
    def information(self):
        info = {
            "id": self.id,
            "text": self.doc_id.text,
            "file": self.doc_id.file,
            "stage": self.stage_id.information() if self.stage_id else {},
            "teacher": self.stage_id.teacher_id.information() if self.stage_id.teacher_id else {},
            "deadline": self.deadline,
            "create_time": self.create_time.strftime("%Y-%m-%d"),
        }
        return info

    # 该任务下学生提交的所有文档
    def student_docs(self):
        docs = Doc.objects.filter(mission_id=self)
        ans = []
        for doc in docs:
            if not self.doc_id.id == doc.id:
                ans.append(doc.information())
        return ans


# 文稿表
class Doc(models.Model):
    # 文档ID
    id = models.AutoField(primary_key=True)
    # 文稿文本
    text = models.TextField(blank=True, null=True)
    # 附件网络路径,长度限制为2048(URL支持的最大长度),有可能在后续版本中,使用models.URLField
    file = models.CharField(max_length=2048, null=True, blank=True)
    # 文稿得分
    score = models.PositiveSmallIntegerField(default=0)
    # 对应任务的ID
    mission_id = models.ForeignKey("Mission", on_delete=models.SET_NULL, blank=True, null=True)
    # 文稿提交用户
    user_id = models.ForeignKey("User", on_delete=models.SET_NULL, blank=True, null=True)
    # 文稿提交时间
    upload_time = models.DateTimeField(auto_now_add=True)

    # Unicode字符串
    def __unicode__(self):
        return json.dumps(self.information())

    # 获取字典格式的文稿信息
    def information(self):
        info = {
            "id": self.id,
            "text": self.text,
            "file": self.file,
            "score": self.score,
            "mission": self.mission_id.information() if self.mission_id else {},
            "user": self.user_id.information() if self.user_id else {},
            "upload_time": self.upload_time.strftime("%Y-%m-%d"),
        }
        return info


# 验证码池
class VerificationCode(models.Model):
    # 验证码ID
    id = models.AutoField(primary_key=True)
    # 对应手机号
    phone = models.CharField(max_length=15)
    # 功能.U:通用,L:登陆
    method = models.CharField(max_length=2)
    # 验证码
    code = models.CharField(max_length=10)
    # 验证码创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 验证码报废时间
    waste_time = models.DateTimeField(auto_now_add=True)
    # 验证码是否使用过
    used = models.BooleanField(default=False)
