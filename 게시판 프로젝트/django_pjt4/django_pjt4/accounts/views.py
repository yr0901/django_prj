from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from reviews.models import Review, Movie, Comment
User = get_user_model()

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form':form
    }
    return render(request, 'accounts/form.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/form.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('index')

@login_required
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    reviews = Review.objects.filter(user_id=pk)
    comments = Comment.objects.filter(user_id=pk)
    context = {
        'user' : user,
        'reviews':reviews,
        'comments':comments,
    }
    return render(request, 'accounts/user_detail.html', context)

@login_required
def follow(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user != request.user:
        if user.followers.filter(pk=request.user.pk).exists():
            user.followers.remove(request.user)

        else:
            user.followers.add(request.user)
    return redirect('accounts:user_detail', user.pk)