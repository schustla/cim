#!/usr/bin/env python
#coding=utf8
'''
Created on 2018/11/30

@author: schustla
@description:
'''
from django.contrib import admin
from ..models import Config

@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    '''配置后台管理'''
    list_display = ['department','random','self_weight','higher_weight','relevant_weight']
    filter_horizontal = ['assessment']