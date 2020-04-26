from django.shortcuts import render, redirect, get_object_or_404
from .models import Review, Comment
from .forms import ReviewForm, CommentForm

def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/review_list.html', context)

def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/form.html', context)

def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.order_by('-pk')
    comment_form = CommentForm()
    context = {
        'review': review,
        'comments': comments,
        'comment_form':comment_form,
    }
    return render(request, 'community/review_detail.html', context)

def update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.user.id == review.user_id:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                review = form.save()
                return redirect('community:detail', review.pk)
        else:
            form = ReviewForm(instance=review)
        context = {
            'form' : form
        }
        return render(request, 'community/form.html', context)
    return redirect('community:index')

def delete(request, id):
    review = get_object_or_404(Review, pk=id)
    if request.user.id == review.user_id:
        if request.method=='POST':
            review.delete()
            return redirect('community:index')
    else:
        return redirect('community:index')

def comments_create(request, review_pk):
    review = get_object_or_404(Review,  pk=review_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review_id = review_pk
            comment.user_id = request.user.pk
            comment.save()
    return redirect('community:detail', review_pk)

def comments_delete(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user.pk == comment.user_id:
        if request.method == 'POST':
            comment.delete()
    return redirect('community:detail', review_pk)