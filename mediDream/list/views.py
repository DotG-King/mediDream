from django.shortcuts import render

# Create your views here.

def search_history(request) :
    user=request.user

    if user.is_authenticated:
        try :
            history=History.objects.all().filter(user=user)
            return render(request, 'history.html',{'history':history})
        except :
            messages.error(request,'history does not exist')
    return render(request, 'history.html')