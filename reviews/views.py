from django.shortcuts import render, redirect

from .forms import ReviewForm
from .models import Review


def review_list(request):
    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/review_list.html', context)


def review_detail(request, pk):
    review = Review.objects.get(pk=pk)

    context = {
        'review': review,
    }

    return render(request, 'reviews/review_detail.html', context)


def review_create(request):
    form = ReviewForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('review-list')

    context = {
        'form': form,
    }

    return render(request, 'reviews/review_form.html', context)


def review_update(request, pk):
    review = Review.objects.get(pk=pk)
    form = ReviewForm(request.POST or None, instance=review)

    form.fields['game'].disabled = True


    if form.is_valid():
        form.save()
        return redirect('review-detail', pk=review.pk)

    context = {
        'form': form,
    }

    return render(request, 'reviews/review_form.html', context)


def review_delete(request, pk):
    review = Review.objects.get(pk=pk)

    if request.method == 'POST':
        review.delete()
        return redirect('review-list')

    context = {
        'review': review,
    }

    return render(request, 'reviews/review_confirm_delete.html', context)
