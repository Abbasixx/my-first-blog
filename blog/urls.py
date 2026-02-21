# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 11:49:21 2026

@author: novin.toos
"""

from django.urls import path
from . import views

urlpatterns= [
    path('', views.post_list, name='post_list'),
]