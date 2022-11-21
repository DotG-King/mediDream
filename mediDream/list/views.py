from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def list_view(request):
    return HttpResponse('리스트 페이지 입니다')

# def search_history(request) :
#     user=request.user

#     if user.is_authenticated:
#         try :
#             history=History.objects.all().filter(user=user)
#             return render(request, 'history.html',{'history':history})
#         except :
#             messages.error(request,'history does not exist')
#     return render(request, 'history.html')

# def pill_info(request) :
#     a=1