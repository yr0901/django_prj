from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from community.models import Review, Comment

# Create your views here.
User = get_user_model()

def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # username = request.POST['username']
            # password = request.POST['password1']

            auth_login(request, user)
            return redirect('community:index')
    else:
        form = UserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method =='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('community:index')
    else:
        form = AuthenticationForm()

    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('community:index')

@login_required
def mypage(request, user_pk):
    reviews = Review.objects.filter(user_id=user_pk)
    comments = Comment.objects.filter(user_id=user_pk)
    context = {
        'reviews':reviews,
        'comments': comments,
    }
    return render(request, 'accounts/mypage.html', context)
