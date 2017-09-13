# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from random import choice
from string import ascii_letters

def main(request):
    if request.method == "POST":
        request.session.flush()
        if request.POST.get("session") == 'true':
            request.session["sessionid"] = str(print(''.join(choice(ascii_letters) for i in range(16))))
            return render(request, "inside.html")
        else:
            return render(request, "auth.html")

    if request.COOKIES.get("vk_app_6180474") is None:
        return render(request, "auth.html")

    if request.COOKIES.get("sessionid") is None:
        return render(request, "auth.html")

    return render(request, "inside.html")