from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse

# Create your views here.

def login_view(request) :
    return HttpResponse('로그인 페이지 입니다')