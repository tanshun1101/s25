"""
用户账户相关功能：注册、短信、登陆、注销
"""
from django.shortcuts import render


def register(request):
    return render(request, 'web/register.html')