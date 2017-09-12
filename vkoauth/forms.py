# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.Form):
    uid = forms.IntegerField()
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    """
    photo = forms.CharField(max_length=255)
    photo_rec = forms.CharField(max_length=255)
    hash_sum = forms.CharField(max_length=255)
    """
    def save(self):
        return User.objects.create(**self.cleaned_data)
       
        
        
        
        
        
        
        
        
        
