from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm, CommentForm
from .models import Review, Comment, Movie
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context ={
        'movies':movies
    }
    return render(request, 'reviews/index.html', context)


def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie':movie
    }
    return render(request, 'reviews/movie_detail.html', context)

# def review_index(request):
#     reviews = Review.objects.all()
#     context = {
#         'reviews':reviews
#     }
#     return render(request, 'review_index.html', context)

@login_required
def review_create(request, movie_pk):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('reviews:review_detail', movie_pk, review.pk)
    else:
        form = ReviewForm()
    context = {
        'form':form
    }
    return render(request, 'reviews/review_create.html', context)


def review_detail(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    context = {
        'review':review
    }
    return render(request, 'reviews/review_detail.html', context)

def review_update(request, movie_pk, review_pk):
    user = get_user_model()
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return redirect('reviews:review_detail', movie_pk, review_pk)

        else:
            form = ReviewForm(instance=review)
        context = {
            'form':form
        }
        return render(request, 'reviews/review_create.html', context)
    else:
        return redirect('reviews:review_detail', movie_pk, review_pk)


def review_delete(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = get_user_model()
    if request.user == user:
        if request.method == 'POST':
            review.delete()
            redirect('reviews:review_index')
    return redirect('reviews:review_detail', movie_pk, review_pk)

@login_required
def comment_create(request, movie_pk, review_pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('reviews:review_detail', movie_pk, review_pk)
    else:
        form = CommentForm()
    context = {
        'form':form,
        'review_pk':review_pk,
        'movie_pk':movie_pk,
    }
    return render(request, 'reviews/comment_create.html', context)

# def comment_update(request, movie_pk, review_pk, comment_pk):
#     comment = get_object_or_404(Comment, pk=comment_pk)
#     if request.user == comment.user:
#         if request.method == 'POST':
#             form = CommentForm(request.POST, instance=comment)
#             if form.is_valid():
#                 form.save()
#                 return redirect('reviews:review_detail', movie_pk, review_pk)
#         else:
#             form = CommentForm(instance=comment)
#         context = {
#             'form':form
#         }
#         return render(request, 'reviews/comment_create.html', context)
#     else:
#         return redirect('reviews:review_detail', movie_pk, review_pk)

def comment_delete(request, movie_pk, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        if request.method == 'POST':
            comment.delete()
            return redirect('reviews:review_detail', movie_pk, review_pk)

    return redirect('reviews:review_detail', movie_pk, review_pk)