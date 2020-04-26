from django.shortcuts import render,redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm
from django.views.decorators.http import require_POST

# Create your views here.

def review_list(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews' : reviews
    }
    return render(request, 'community/review_list.html', context)

def create(request):
    if request.method =='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()

    context = {
        'form':form
    }
    return render(request, 'form.html', context)

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    context = {
        'review' : review
    }
    return render(request, 'community/review_detail.html',context)

#@require_POST
def review_delete(request, pk):
    if request.method == 'POST':
        review = get_object_or_404(Review, pk=pk)
        review.delete()
        return redirect('community:index')

    else:
        reviews = Review.objects.order_by('-pk')
        context = {
            'reviews':reviews,
            'some_flag':True
        }
        return render(request, 'community/review_list.html', context)

def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect('community:detail', review.pk)

    else:
        form = ReviewForm(instance=review)

    context = {
        'form':form
    }
    return render(request, 'community/form.html', context)