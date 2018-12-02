# -*- coding: utf-8 -*-
from django.contrib import admin
# 导入我们要注册的模型
from learning_logs.models import Topic, Entry

# 让 Django 通过管理网站管理我们的模型
admin.site.register(Topic)
admin.site.register(Entry)
