#!/usr/bin/env python
#coding=utf8
'''
Created on 2018/11/21

@author: schustla
'''
from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
from django.contrib import auth
from django.http import HttpResponseRedirect



@login_required
def index(request):
    '''职业规划首页'''
    context = {}
    return  render(request,'career/index.html',context)