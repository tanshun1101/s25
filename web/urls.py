"""s25 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from web.views import account
from web.views import home
from web.views import project
urlpatterns = [
    # 加上name方便解析
    url(r'^register/$', account.register, name='register'),  # register
    url(r'^login/sms/$', account.login_sms, name='login_sms'),  # send_sms
    url(r'^login/$', account.login, name='login'),
    url(r'^image/code$', account.image_code, name='image_code'),
    url(r'^send/sms/$', account.send_sms, name='send_sms'),  # send_sms
    url(r'^logout/$', account.logout, name='logout'),  # send_sms
    url(r'^index/$', home.index, name='index'),

    # 项目管理
    url(r'^project/list$', project.project_list, name='project_list'),

]
