from django.shortcuts import render, redirect
from django.urls import reverse
from apps.user.models import User
import re


# Create your views here.
# user/register
def register(request):
    """显示注册页面"""
    return render(request, "register.html")


def register_handler(request):
    """处理注册页面"""
    # 获取值
    user_name = request.POST.get("user_name")
    pwd = request.POST.get("pwd")
    cpwd = request.POST.get("cpwd")
    email = request.POST.get("email")
    allow = request.POST.get("allow")
    # 校验数据
    if not all([user_name, pwd, cpwd, email, allow]):
        return render(request, "register.html", {"errmsg": "信息不全"})

    if not re.match(r"^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$", email):
        return render(request, "register.html", {"errmsg": "邮箱格式不对"})

    if pwd != cpwd:
        return render(request, "register.html", {"errmsg": "两次密码不一致"})

    if allow != "on":
        return render(request, "register.html", {"errmsg": "不同意协议"})

    # 校验是否存在
    try:
        user = User.objects.get(username=user_name)
    except User.DoesNotExist:
        user = None

    if user:
        return render(request, "register.html", {"errmsg": "用户名已经存在"})

    # 保存用户到数据库
    user = User.objects.create_user(user_name, email, pwd)
    user.is_active = 0
    user.save()

    # 反向解析重定向到首页
    return redirect(reverse("goods:index"))
