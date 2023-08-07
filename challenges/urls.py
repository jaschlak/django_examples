# -*- coding: utf-8 -*-

from django.urls import path

from . import views

urlpatterns = [
        #/challenges/january
        #path("january",views.january),
        #path("february",views.february),
        path("<month>", views.monthly_challenge),
    ]