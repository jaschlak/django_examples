# -*- coding: utf-8 -*-

from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField()
    