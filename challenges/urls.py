# -*- coding: utf-8 -*-

from django.urls import path

from . import views


urlpatterns = [
        #/challenges/january
        #path("january",views.january),
        #path("february",views.february),
        
        # dynamic
        #path("<month>", views.monthly_challenge),
        
        # dynamic with input type filters (top down)
        path("<int:month>", views.monthly_challenge_by_number),
        path("<str:month>", views.monthly_challenge),
    ]