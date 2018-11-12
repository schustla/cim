#!/usr/bin/env python
#coding=utf8
'''
Created on 2018/11/30

@author: schustla
@description:
'''
from django.shortcuts import render
from django.contrib.auth.decorators import  login_required



@login_required
def detail(request):
    '''详情'''
    context= {}
    context["performanceActive"]= "active"

    return render(request,'performance/detail.html',context=context)