# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("<h2>Hey Praw!!</h2>")