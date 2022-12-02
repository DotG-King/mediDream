from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

LOGIN_TRY_LIMIT=5
count=0

def main(request):
    user=request.user
    return render(request,'accounts/main.html', {'user':user})

#회원가입
def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]: 
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"],
                email=request.POST['email'],)
            auth.login(request,user)
            return redirect('login') #account.urls의 name(회원가입후 들어가는 페이지)
        return render(request, 'accounts/signup.html')    
    return render(request, 'accounts/signup.html')  

#로그인
def login(request) :
    if request.method == "POST":
        global count
        username=request.POST["username"]
        password=request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            count=0
            auth.login(request,user)
            return redirect('main') #로그인이 성공하면 search.urls로 넘어감           
        else:
            count=count+1
            err_msg='아이디 or 비밀번호 '+str(count)+'회 오류입니다.'
            if (count >= LOGIN_TRY_LIMIT) :
                return render(request, 'accounts/login.html', {'error': '3분간 로그인을 금지합니다.', 'count':count})
            return render(request, 'accounts/login.html', {'error':err_msg}) #에러코드 출력하면서 login 페이지 보여줌
    else:
        return render(request, 'accounts/login.html') 
        


def logout(request):
    auth.logout(request)
    return redirect('login') #로그아웃하면 최초 페이지로 돌아감