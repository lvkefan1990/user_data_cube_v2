"""user_data_cube_v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from user_data_cube import jump
from user_data_cube import submit

urlpatterns = [
    path(r'admin/', admin.site.urls),#跳转至admin管理页面
    path(r'', jump.user_login),#跳转至登录页面
    path(r"login/", jump.user_login),#跳转至登录页面
    path(r'index/', jump.index),#跳转至主页面
    path(r'wlgz/', jump.wlgz,name="wlgz"),#跳转至网络感知界面
    path(r'lssj/', jump.lssj,name="lssj"),#跳转至历史事件界面
    path(r'scpg/', jump.scpg,name="scpg"),#跳转至市场评估界面
    path(r'yhty/', jump.scpg,name="yhty"),#跳转至用户体验界面
    path(r'exit/', jump.exit),#跳转至退出
    path(r'change_password/', jump.change_password),#修改密码
    path(r'login_submit/', submit.login_submit),#提交用户名和密码
    path(r'wlgz_submit/', submit.wlgz_submit),#无线感知提交用户名和密码
    path(r'scpg_submit/', submit.scpg_submit),  # 市场评估提交用户名和密码
    path(r'lssj_submit/', submit.lssj_submit),#历史数据提交用户名和密码
]
