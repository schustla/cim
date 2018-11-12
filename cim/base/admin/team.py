#!/usr/bin/env python
#coding=utf8
'''
Created on 2018/11/13

@author: schustla
'''

from django.contrib import admin

from ..models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    filter_horizontal = ['member']
    fieldsets = [
        (u'项目名称', {
            'fields': ['name','is_active'],
        }),
        (u'项目成员',{
            'fields':['member'],
        })
    ]