from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from .models import Review, Comment
from django import forms

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields =  ['username', 'first_name', 'last_name', 'email']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields =['title','movie_title','rank','content',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =['content']