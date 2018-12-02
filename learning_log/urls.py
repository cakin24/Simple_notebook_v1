# -*- coding: utf-8 -*-
# 导入了为项目和管理网站管理 URL 的函数和模块
from django.conf.urls import include, url
from django.contrib import admin
# 这个文件的主体定义了变量 urlpatterns
# 变量 urlpatterns 包含项目中的应用程序的 URL
urlpatterns = [
    # 包含模块 admin.site.urls ，该模块定义了可在管理网站中请求的所有 URL 。
    url(r'^admin/', include(admin.site.urls)),
    # 我们添加了一行代码来包含模块 learning_logs.urls 。
    # 这行代码包含实参 namespace ，让我们能够将 learning_logs 的 URL 同项目中的其他 URL 区分开来，
    # 这在项目开始扩展时很有帮助。
    url(r'', include('learning_logs.urls', namespace='learning_logs')), 
]
