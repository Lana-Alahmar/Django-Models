# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 11:24:35 2022

@author: Classic
"""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
