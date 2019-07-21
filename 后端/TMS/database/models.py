#!/usr/bin/env python
# -*- coding:utf-8 -*-


from django.db import models


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


# 班级表
class Class(models.Model):
    # 班级id
    id = models.AutoField(primary_key=True)
    # 班级名称
    name = models.CharField(max_length=128)
    # 上课教室
    room = models.CharField(max_length=128)


# 可选项目池
class ProjectPool(models.Model):
    # 可选项目ID
    id = models.AutoField(primary_key=True)
    # 可选项目名称
    name = models.CharField(max_length=128)
    # 可选项目简介
    content = models.TextField(blank=True, null=True)


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
