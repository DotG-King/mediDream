from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def search_view(request) :
    return HttpResponse('검색 페이지 입니다.')