# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings








def test(request):
    if request.COOKIES.get("vk_app_6180474") is None:
        return render(request, "get.html")
    else:
        return render(request, "post.html")