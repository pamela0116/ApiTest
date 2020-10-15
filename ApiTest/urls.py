"""ApiTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path

from MyApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', welcome),  # 获取菜单
    path('home/', home),  # 进入首页
    re_path(r'^child/(?P<eid>.+)/(?P<oid>.*)/$',child),
    path('login/', login),  # 进入登录页面
    path('login_action/', login_action),  # 登录
    path('register_action/', register_action),  # 注册
    path('accounts/login/', login),  # 非登录状态自动跳到登录页面
    path('logout/', logout),  # 退出登录
    path('pei/', pei),  # 匿名吐槽
    path('help/', api_help),  # 进入帮助文档页面
    path('project_list/', project_list),  # 进入项目列表页面
    path('delete_project/', delete_project),  # 删除项目
    path('add_project/', add_project),  # 新增项目
    re_path(r'^apis/(?P<id>.*)/$', open_apis),  # 进入接口库
    re_path(r'^cases/(?P<id>.*)/$', open_cases),  # 进入用例设置库
    re_path(r'^project_set/(?P<id>.*)/$', open_project_set),  # 进入项目设置
    re_path(r'^save_project_set/(?P<id>.*)/$', save_project_set),  # 保存项目设置
    re_path(r'^project_api_add/(?P<Pid>.*)/$', project_api_add),  # 新增接口 Pid:项目id
    re_path(r'^project_api_del/(?P<id>.*)/$', project_api_del),  # 删除接口
    re_path(r'^save_bz/$', save_bz),  # 保存备注
    re_path(r'^get_bz/$', get_bz),  # 获取备注
    re_path(r'^Api_save/$', Api_save),  # 保存接口
    re_path(r'^get_api_data/$', get_api_data),  # 获取接口数据
    re_path(r'^Api_send/$', Api_send),  # 调试层发送请求
    re_path(r'^copy_api/$', copy_api),  # 复制接口
    re_path(r'^error_request/$', error_request),  #调用异常测试接口
]
