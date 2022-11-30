from django.shortcuts import render, redirect
from django.http import HttpResponse
from list.models import search, pillInfo


# Create your views here.

def list_view(request):
    user=request.user
    if(user.is_authenticated):
        history=search.objects.all().filter(mediDream_id=user)
        return render(request, 'list/history.html', {'history':history, 'user':user})
    else :
        return render(request, 'list/history.html', {'user':user})
    
def pill_info(request, word):
    pill=pillInfo.objects.all().filter(id=word)
    return render(request, 'list/info.html', {'pill':pill})