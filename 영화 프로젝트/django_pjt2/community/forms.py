from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        label='리뷰 제목',
        widget = forms.TextInput(
            attrs = {
                'placeholder':'리뷰 제목을 입력하세요'
            }

            )
        )

    movie_title = forms.CharField(
        max_length=30,
        label = '영화 제목',
        widget = forms.TextInput(
            attrs = {
                'placeholder':'영화 제목을 입력하세요'
            }
            )
        )

    content = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                'placeholder':'내용을 입력하세요'
            }
            )
        )
    class Meta:
        model = Review
        fields = ['title','movie_title','rank','content']