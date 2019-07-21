"""TMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings
from . import views

urlpatterns = [
    # 主视图界面
    path("", views.index),
    # 管理员界面,暂时无用,先保留
    path("admin/", admin.site.urls),
    # api应用url,指向api/urls
    re_path("api/?", include("api.urls")),
    # 数据库视图接口,测试时使用
    re_path("database/?", include("database.urls")),
    # 媒体文档文件静态目录
    re_path(r"file/(?P<path>.*)", serve, {"document_root": settings.FILE_ROOT}),

    path('login', views.login),
    re_path(r"admin_teacher/?", views.admin_teacher),
    re_path(r"admin_student/?", views.admin_student),
    re_path(r"admin_Class_Page/?", views.class_page),
    re_path(r"stu_doc_check/?", views.doc_check),
    re_path(r"stu_select_pro/?", views.select_project),
    re_path(r"stu_check_task/?", views.check_task),

    # 配置静态资源,可以直接通过url访问static目录下的文件,!!!需要放置在最后一条路由规则!!!
    re_path(r"(?P<path>.*)", serve, {"document_root": settings.PUBLIC_ROOT}),
]
