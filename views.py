from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

now = datetime.now()
def home(requests):
    return HttpResponse("hello django world")
def greeting(requests):
    return HttpResponse("greeting")
def introduction(requests):
    return HttpResponse("introduction")
def current_time(requests):
    return HttpResponse(now)
def dict_(requests):
    dict_ = {}
    for i in range(1, 16):
        dict_[i] = i ** 2
    return HttpResponse(f'{dict_}')
