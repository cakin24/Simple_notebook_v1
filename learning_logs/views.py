# -*- coding: utf-8 -*-
'''
视图函数接受请求中的信息，准备好生成网页所需的数据，再将这些数据发送给浏览器
'''
from django.shortcuts import render
# 导入了与所需数据相关联的模型
from .models import Topic

def index(request):
    """ 学习笔记的主页
    URL 请求与我们刚才定义的模式匹配时， Django 将在文件 views.py 中查找函数 index() ，再将请求对象传递给这个视图函数。
    在这里，我们不需要处理任何数据，因此这个函数只包含调用 render() 的代码。
    这里向函数 render() 提供了两个实参：原始请求对象以及一个可用于创建网页的模板。
    """
    return render(request, 'learning_logs/index.html')

# 函数 topics() 包含一个形参： Django 从服务器那里收到的 request 对象
def topics(request):
    """显示所有主题"""
    # 我们查询数据库 —— 请求提供 Topic 对象，并按属性 date_added 对它们进行排序。
    # 我们将返回的查询集存储在 topics 中。
    topics = Topic.objects.order_by('date_added')
    # 我们定义了一个将要发送给模板的上下文。
    # 上下文是一个字典，其中的键是我们将在模板中用来访问数据的名称，而值是我们要发送给模板的数据。
    # 在这里，只有一个键 — 值对，它包含我们将在网页中显示的一组主题。
    context = {'topics': topics}
    # 创建使用数据的网页时，除对象 request 和模板的路径外，我们还将变量 context 传递给 render()
    return render(request, 'learning_logs/topics.html', context)

'''
这是第一个除 request 对象外还包含另一个形参的视图函数。
这个函数接受正则表达式 (?P<topic_id>\d+) 捕获的值，并将其存储到 topic_id 中。
我们使用 get() 来获取指定的主题
我们获取与该主题相关联的条目，并将它们按 date_added 排序： 
date_added 前面的减号指定按降序排列，即先显示最近的条目。
我们将主题和条目都存储在字典 context 中，再将这个字典发送给模板 topic.html。
在自己的项目中编写查询时，先在 Django shell 中进行尝试大有裨益。
相比于编写视图和模板，再在浏览器中检查结果，在 shell 中执行代码可更快地获得反馈。
'''
def topic(request, topic_id):
    """ 显示单个主题及其所有的条目 """
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
