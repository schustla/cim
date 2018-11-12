#!/usr/bin/env python
#coding=utf8
'''
Created on 2018/11/19

@author: schustla
'''
from  django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^index/$',views.index,name='index'),

]