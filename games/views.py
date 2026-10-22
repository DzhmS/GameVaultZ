from django.shortcuts import render, redirect, get_object_or_404

from .forms import GameForm, GenreForm
from .models import Game, Genre
from platforms.models import Platform


def game_list(request):
    sort = request.GET.get('sort', 'title')
    genre_id = request.GET.get('genre')
    platform_id = request.GET.get('platform')

    allowed_sorts = [
        'title',
        '-title',
        'release_date',
        '-release_date',
    ]

    if sort not in allowed_sorts:
        sort = 'title'

    games = Game.objects.all()
    genres = Genre.objects.all()
    platforms = Platform.objects.all()

    if genre_id:
        games = games.filter(genres__pk=genre_id)

    if platform_id:
        games = games.filter(platforms__pk=platform_id)

    games = games.order_by(sort)

    context = {
        'games': games,
        'genres': genres,
        'platforms': platforms,

        'selected_genre': genre_id,
        'selected_platform': platform_id,
        'selected_sort': sort,
    }

    return render(request, "games/game_list.html", context)


def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)

    context = {
        'game': game,
    }
    return render(request, "games/game_detail.html", context)


def game_create(request):
    form = GameForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('game-list')

    context = {
        'form': form,
    }

    return render(request, "games/game_form.html", context)


def game_update(request, pk):
    game = get_object_or_404(Game, pk=pk)

    form = GameForm(
        request.POST or None,
        request.FILES or None,
        instance=game
    )

    if form.is_valid():
        form.save()
        return redirect('game-detail', pk=game.pk)

    context = {
        'form': form,
    }

    return render(request, 'games/game_form.html', context)

def game_delete(request, pk):
    game = get_object_or_404(Game, pk=pk)

    if request.method == 'POST':
        game.delete()
        return redirect('game-list')

    context = {
        'game': game,
    }

    return render(request, 'games/game_confirm_delete.html', context)


def genre_list(request):
    genres = Genre.objects.all()

    context = {
        'genres': genres,
    }

    return render(request, 'genres/genre_list.html', context)


def genre_detail(request, pk):
    genre = get_object_or_404(Genre, pk=pk)

    context = {
        'genre': genre,
    }

    return render(request, 'genres/genre_detail.html', context)


def genre_create(request):
    form = GenreForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('genre-list')

    context = {
        'form': form,
    }

    return render(request, 'genres/genre_form.html', context)


def genre_update(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    form = GenreForm(request.POST or None, instance=genre)

    if form.is_valid():
        form.save()
        return redirect('genre-detail', pk=genre.pk)

    context = {
        'form': form,
    }

    return render(request, 'genres/genre_form.html', context)


def genre_delete(request, pk):
    genre = get_object_or_404(Genre, pk=pk)

    if request.method == 'POST':
        genre.delete()
        return redirect('genre-list')

    context = {
        'genre': genre,
    }

    return render(request, 'genres/genre_confirm_delete.html', context)