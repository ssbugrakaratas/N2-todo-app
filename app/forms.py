"""
Copyright (c) 2022 - present Samed Buğra KARATAŞ
"""

from email.policy import default
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=256)
    password = forms.CharField(max_length=256)