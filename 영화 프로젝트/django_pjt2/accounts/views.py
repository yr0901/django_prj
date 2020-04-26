from django.shortcuts import render
# 각 문제를 해결하기 위하여 필요한 import문은 이곳에 작성합니다.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from django.contrib.auth import login as auth_login, logout as auth_logout

def index(request):
    return render(request, 'accounts/index.html')

def signup(request):
    # Q1-1
    #요청이 POST방식으로 들어온 경우, 즉 정보를 기입하고 SUBMIT을 한 경우
    if request.method == 'POST':
        form = UserCreationForm(request.POST) #작성된 유저정보를 request.POST를 통해 가져온다
        if form.is_valid(): # 해당 form 이 유효한지 확인한다.
            form.save() # 유저 정보를 저장한다.
            return redirect('accounts:index')
    #method가 GET으로 들어올 경우, 회원가입을 위한 폼을 보내준다.
    else:
        form = UserCreationForm() #빈 폼 생성

    context = {
        'form':form,
    }

    return render(request, 'accounts/form.html', context)

def login(request):
    # Q1-2
    #요청이 post방식으로 들어온 경우, 즉 로그인 정보 입력 후 submit을 누른 경우
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST) #login을 위한 정보를 request.POST로 가져와서 AuthenticationForms에 넣는다.
        #이때 authenticationForm은 UserCreationForm과 다르게 그냥 form을 상속받고 있기 때문에 첫번째 인자로 request를 필요로 한다.
        if form.is_valid(): #form이 유효한지 판단
            auth_login(request, form.get_user()) #import 해온 auth_login으로 login을 진행한다. 
            #form에 있는 유저정보를 가져오기 위해 get_user() 함수를 사용한다.
            return redirect('accounts:index')
    
    #요청이 get방식으로 들어온 경우, 즉 login 정보를 입력하기 위한 요청이 들어온 경우
    else:
        form = AuthenticationForm() #로그인 할 수 있는 빈 폼을 생성한다.
    context = {
        'form':form
    }
    return render(request, 'accounts/form.html', context)


def logout(request):
    # Q1-3
    # a 태그는 기본적으로 GET방식으로 들어오기 때문에 별다른 설정을 해줄 필요가 없다.
    auth_logout(request) #import 해온 auth_logout을 이용해 로그아웃 한다.
    return redirect('accounts:index')