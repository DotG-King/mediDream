from django.shortcuts import render, redirect
from django.http import HttpResponse
from list.models import search, pillInfo


# Create your views here.

def list_view(request):
    # 로그인 기능 생기면 request에서 유저 확인하는 기능과 연결 필요
    user=request.user

    if(user.is_authenticated):
        test=search.objects.all().filter(mediDream_id=user)
        for item in test :
            print('{0}, {1}, {2}, {3}\n'.format(user,item.mediDream_id.username, item.pill.pill_name, item.date))
        return render(request, 'list/history.html', {'test':test, 'user':user})
    else :
        # return redirect('login')
        return render(request, 'list/history.html', {'user':user})
    
def pill_info(request, word):
    test=pillInfo.objects.all().filter(id=word)
    print(test)
    for item in test :
        print('{0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(item.pill_name,item.pill_effect,item.pill_usage,item.pill_caution,item.pill_color,item.pill_shape,item.pill_engrave))
    return render(request, 'list/info.html', {'test':test})