#!/usr/bin/env python
#coding=utf8
'''
Created on 2018/11/19

@author: schustla
'''
from django.db import models
import  base.models as base

class Answer(models.Model):
    '''答案'''
    content = models.TextField(verbose_name=u'问题答案')
    # user = models.ForeignKey('base.User',verbose_name=u'填写人')
