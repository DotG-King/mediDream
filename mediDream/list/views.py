from django.shortcuts import render
from django.http import HttpResponse
from list.models import search, pillInfo


# Create your views here.

def list_view(request):
    # 로그인 기능 생기면 request에서 유저 확인하는 기능과 연결 필요
    user=request.user
    print(user)
    print(user.is_authenticated)
    test=search.objects.all().filter(mediDream_id=user)
    print(test)

    if(user.is_authenticated):
        for item in test :
            print('{0}, {1}, {2}, {3}\n'.format(user,item.mediDream_id.username, item.pill.pill_name, item.date))
        return render(request, 'list/history.html', {'test':test})
    else :
        return HttpResponse('로그인이 되어있지 않습니다!')

    # if (request.user.is_authenticated) :
    #     try :
    #         test=search.objects.all().filter(mediDream_id=user)
    #         for item in test :
    #             print('{0}, {1}, {2}\n'.format(item.mediDream_id.m_id, item.pill.pill_name, item.date))
    #             if request.user.is_authenticated:
    #                 print("User is logged in :)")
    #                 print(f"Username --> {request.user.username}")
    #             else:
    #                 print("User is not logged in :(")
    #         return render(request, 'list/history.html', {'test':test})
    #     except :
    #         return HttpResponse('로그인이 되어있지 않습니다!')
    
def pill_info(request, word):
    test=pillInfo.objects.all().filter(pill_name=word)
    print(test)
    for item in test :
        print('{0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(item.pill_name,item.pill_effect,item.pill_usage,item.pill_caution,item.pill_color,item.pill_shape,item.pill_engrave))
    # return HttpResponse('약 정보 페이지 입니다.\n list_view에서 {0}약을 누르고 이 페이지로 넘어왔습니다.'.format(word))
    return render(request, 'list/info.html', {'test':test})

# def search_history(request) :
#     user=request.user

#     if user.is_authenticated:
#         try :
#             history=History.objects.all().filter(user=user)
#             return render(request, 'history.html',{'history':history})
#         except :
#             messages.error(request,'history does not exist')
#     return render(request, 'history.html')