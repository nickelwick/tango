# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says hello world! <a href='about'>link</a>")

def about(request):
	return HttpResponse("About page")

