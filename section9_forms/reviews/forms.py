# -*- coding: utf-8 -*-

from django import forms

class ReviewForm(forms.Form):
    
    user_name = forms.CharField(label="Your Name", required=True, max_length=100, error_messages={
            "required": "Your name must not be empty like your soul",
            "max_length": "Please enter a shorter name!"
        })
    