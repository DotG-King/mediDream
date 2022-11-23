from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
#authenticate ->User 인증 함수. 자격 증명이 유효한 경우 User 객체를, 그렇지 않은 경우 None을 반환

#회원가입
def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]: 
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"],)
            auth.login(request,user)
            return redirect('login') #account.urls의 name(회원가입후 들어가는 페이지)
        return render(request, 'accounts/signup.html')    
    return render(request, 'accounts/signup.html')  

#로그인
def login(request) :
    if request.method == "POST": 
        username=request.POST["username"]
        password=request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:   
            auth.login(request,user)
            return redirect('index') #로그인이 성공하면 search.urls로 넘어감
            
        else:
            return render(request, 'accounts/login.html', {'error':'아이디 or 비밀번호 오류입니다'}) #에러코드 출력하면서 login 페이지 보여줌
    else:
        return render(request, 'accounts/login.html') 


def logout(request):
    auth.logout(request)
    return redirect('login') #로그아웃하면 최초 페이지로 돌아감



