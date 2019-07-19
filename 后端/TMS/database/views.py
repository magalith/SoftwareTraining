from django.shortcuts import render, redirect, HttpResponse


# 测试注册界面
# http://0.0.0.0/database/register
def register(request):
    if request.method == "POST":
        user_name = request.POST.get("user")

        return HttpResponse("")
    return render(request, "database/register.html", {})
