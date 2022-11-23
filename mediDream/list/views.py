from django.shortcuts import render
from django.http import HttpResponse
from list.models import search


# Create your views here.

def list_view(request):
    # 로그인 기능 생기면 request에서 유저 확인하는 기능과 연결 필요
    test=search.objects.all().filter(mediDream_id='t')
    for item in test :
        print('{0}, {1}, {2}\n'.format(item.mediDream_id.m_id, item.pill.pill_name, item.date))
    # return HttpResponse(b)
    return render(request, 'list/history.html', {'test':test})

def pill_info(request, word):
    param={'pname':word}
    # return HttpResponse('약 정보 페이지 입니다.\n list_view에서 {0}약을 누르고 이 페이지로 넘어왔습니다.'.format(word))
    return render(request, 'list/info.html', param)

# def search_history(request) :
#     user=request.user

#     if user.is_authenticated:
#         try :
#             history=History.objects.all().filter(user=user)
#             return render(request, 'history.html',{'history':history})
#         except :
#             messages.error(request,'history does not exist')
#     return render(request, 'history.html')