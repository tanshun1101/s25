#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from django.shortcuts import render


def project_list(request):
    """项目列表"""
    print(request.tracer.user)
    print(request.tracer.price_policy)

    return render(request, 'project_list.html')
