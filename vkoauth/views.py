# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from vkoauth.forms import UserForm


def test(request):    
    if request.method == "POST": 
        user = UserForm(request.POST)
        if user.is_valid():
            user.save()
            login(request, user)
            return render(request, "post.html", {'user' : user})
        else:
            return HttpResponse("I don't know how does it happen")
    else:
        if request.user.is_authenticated():
            return render(request, "post.html", {'user' : user})
        else:
            return render(request, "get.html")  

