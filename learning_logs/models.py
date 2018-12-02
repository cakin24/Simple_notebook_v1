# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

'''
模型就是一个类,包含属性和方法。
'''
'''
用户学习的主题
Model:Django 中一个定义了模型基本功能的类。
属性 text 是一个 CharField,由字符或文本组成的数据.需要存储少量的文本，如名称、标题或城市时，可使用 CharField 。
属性 date_added 是一个 DateTimeField,记录日期和时间的数据
传递了实参 auto_add_now=True ，每当用户创建新主题时，这都让 Django 将这个属性自动设置成当前日期和时间。
字段参考： https://docs.djangoproject.com/en/1.8/ref/models/fields/
'''
class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    # 默认应使用哪个属性来显示有关主题的信息。
    # 如果你使用的是 Python 2.7 ，应调用方法 __unicode__() ，而不是 __str__()
    def __unicode__(self):
        """Return a string representation of the model."""
        return self.text

""" 
学到的有关某个主题的具体知识 
"""
class Entry(models.Model):
    '''
    第一个属性 topic 是一个 ForeignKey 实例
    外键是一个数据库术语，它引用了数据库中的另一条记录；这些代码将每个条目关联到特定的主题。
    每个主题创建时，都给它分配了一个键（或 ID ）。
    需要在两项数据之间建立联系时， Django 使用与每项信息相关联的键。
    根据这些联系获取与特定主题相关联的所有条目。
    '''
    topic = models.ForeignKey(Topic)
    # 这种字段不需要长度限制，因为我们不限制条目的长度。
    text = models.TextField()
    # 属性 date_added 让我们能够按创建顺序呈现条目，并在每个条目旁边放置时间戳。
    date_added = models.DateTimeField(auto_now_add=True)
    '''
    在 Entry 类中嵌套了 Meta 类。
    Meta 存储用于管理模型的额外信息
    它让我们能够设置一个特殊属性，让 Django 在需要时使用 Entries 来表示多个条目。
    如果没有这个类， Django 将使用 Entrys 来表示多个条目。
    '''
    class Meta:
        verbose_name_plural = 'entries'

    '''
    由于条目包含的文本可能很长，我们让 Django 只显示 text 的前 50 个字符
    我们还添加了一个省略号，指出显示的并非整个条目。
    '''
    def __unicode__(self):
        """ 返回模型的字符串表示 """
        return self.text[:50] + "..."
