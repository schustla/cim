# -*- encoding: utf-8 -*-

from  django.apps import AppConfig

class performanceConfig(AppConfig):
    name ='performance'
    verbose_name = u'履约考核管理'

    def ready(self):
        import performance.signals
