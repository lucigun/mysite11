from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request) :
    return HttpResponse("안녕 파이보")