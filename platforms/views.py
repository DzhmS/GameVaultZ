from django.shortcuts import render, redirect

from .forms import PlatformForm
from .models import Platform

def platform_list(request):
    platforms = Platform.objects.all()

    context = {
        'platforms': platforms,
    }

    return render(request, 'platforms/platform_list.html', context)



def platform_detail(request, pk):
    platform = Platform.objects.get(pk=pk)

    context = {
        'platform': platform,
    }

    return render(request, 'platforms/platform_detail.html', context)


def platform_create(request):
    form = PlatformForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('platform-list')

    context = {
        'form': form,
    }

    return render(request, 'platforms/platform_form.html', context)


def platform_update(request, pk):
    platform = Platform.objects.get(pk=pk)
    form = PlatformForm(request.POST or None, instance=platform)

    if form.is_valid():
        form.save()
        return redirect('platform-detail', pk=platform.pk)

    context = {
        'form': form,
    }

    return render(request, 'platforms/platform_form.html', context)


def platform_delete(request, pk):
    platform = Platform.objects.get(pk=pk)

    if request.method == 'POST':
        platform.delete()
        return redirect('platform-list')

    context = {
        'platform': platform,
    }

    return render(request, 'platforms/platform_confirm_delete.html', context)
