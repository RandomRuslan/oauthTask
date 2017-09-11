# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def test(request):
    """  
    error = ''
    if request.method == "POST":
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
                login(request, user)
                return HttpResponseRedirect("/")
        else:
            error = "Incorrect username/password"
    """
    
    return render(request, "login.html")  
    #s = '<p style="margin: 0.4em;"><a href="{% url socialauth_begin \'vkontakte-oauth2\' %}">Enter VK</a></p><br>'
    #return HttpResponse(s+"Rubenchik")
