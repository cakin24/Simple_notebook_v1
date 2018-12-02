# -*- coding: utf-8 -*-
"""
定义 learning_logs 的 URL 模式
导入了函数 url ，因为我们需要使用它来将 URL 映射到视图
"""
from django.conf.urls import url
# 句点让 Python 从当前的 urls.py 模块所在的文件夹中导入视图。
from . import views
# 这个文件的主体定义了变量 urlpatterns
# 变量 urlpatterns 是一个列表，包含可在应用程序 learning_logs 中请求的网页
'''
实际的 URL 模式是一个对函数 url() 的调用，这个函数接受三个实参。
第一个是一个正则表达式。 Django 在 urlpatterns 中查找与请求的 URL 字符串匹配的正则表达式，因此正则表达式定义了 Django 可查找的模式。
我们来看看正则表达式 r'^$' 。其中的 r 让 Python 将接下来的字符串视为原始字符串，而引号告诉 Python 正则表达式始于和终于何处。
脱字符（ ^ ）让 Python 查看字符串的开头，而美元符号让 Python 查看字符串的末尾。
总体而言，这个正则表达式让 Python 查找开头和末尾之间没有任何东西的 URL 。 
Python 忽略项目的基础 URL （ http://localhost:8000/ ），因此这个正则表达式与基础 URL 匹配。
其他 URL 都与这个正则表达式不匹配。如果请求的 URL 不与任何 URL 模式匹配， Django 将返回一个错误页面。
url() 的第二个实参指定了要调用的视图函数。请求的 URL 与前述正则表达式匹配时， Django 将调用 views.index.
第三个实参将这个 URL 模式的名称指定为 index ，让我们能够在代码的其他地方引用它。
每当需要提供到这个主页的链接时，我们都将使用这个名称，而不编写 URL 。
'''
urlpatterns = [
    # 主页.
    url(r'^$', views.index, name='index'),
    
    # 显示所有主题.
    url(r'^topics/$', views.topics, name='topics'),
    
    # 特定主题详细页面
    # r 让 Django 将这个字符串视为原始字符串，并指出正则表达式包含在引号内。
    # 这个表达式的第二部分（ /(?P<topic_id>\d+)/ ）与包含在两个斜杠内的整数匹配，并将这个整数存储在一个名为 topic_id 的实参中。
    # 这部分表达式两边的括号捕获 URL 中的值； ?P<topic_id> 将匹配的值存储到 topic_id 中；
    # 而表达式 \d+ 与包含在两个斜杆内的任何数字都匹配，不管这个数字为多少位。
    #  URL 与这个模式匹配时， Django 将调用视图函数 topic() ，并将存储在 topic_id 中的值作为实参传递给它。
    # 在这个函数中，我们将使用 topic_id 的值来获取相应的主题。
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
