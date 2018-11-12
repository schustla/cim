#!/usr/bin/env python
#coding=utf8
'''
Created on 2018/11/22

@author: schustla
@description:相关人设置
'''
from  django.db import models


class Stakeholder(models.Model):
    '''相关人'''

    person = models.ForeignKey('base.User', related_name='person',verbose_name=u'拥有者',unique=True)
    higher = models.ManyToManyField('base.User',related_name='higher',verbose_name=u'高级相关人',null=True,blank=True)
    stakeholder = models.ManyToManyField('base.User',related_name='stakeholder',verbose_name=u'普通相关人',null=True,blank=True)

    def is_active(self):
        '''有效'''
        if  self.person.is_active:

            return u'有效'
        else:
            return u'无效'
    is_active.short_description = u"有效"
    is_active_str = property(is_active)
    def __unicode__(self):
        if self.person:

            return self.person.username_zh
        else:
            return '-'

    class Meta:
        verbose_name = u'相关人'
        verbose_name_plural = u'相关人管理'


class ResultCheck(models.Model):
    """结果查看"""
    user = models.ForeignKey('base.User',related_name='check_user',verbose_name=u'查看人',unique=True)
    department = models.ManyToManyField('base.Department',related_name='check_department',verbose_name=u'部门')

    def __unicode__(self):
        if self.user:

            return self.user.username_zh
        else:
            return '-'

    class Meta:
        verbose_name = u'结果查看'
        verbose_name_plural = u'结果查看管理'