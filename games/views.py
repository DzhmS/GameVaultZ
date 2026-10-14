from django.shortcuts import render,redirect

from .forms import GameForm, GenreForm
from .models import Game, Genre


def game_list(request):
    games = Game.objects.all()

    context = {
        'games': games,
    }

    return render(request, "games/game_list.html", context)


def game_detail(request, pk):
    game = Game.objects.get(pk=pk)

    context = {
        'game': game,
    }
    return render(request, "games/game_detail.html", context)


def game_create(request):
    form = GameForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('game-list')

    context = {
        'form': form,
    }

    return render(request, "games/game_form.html", context)

def game_update(request, pk):
    game = Game.objects.get(pk=pk)
    form = GameForm(request.POST or None, instance=game)

    if form.is_valid():
        form.save()
        return redirect('game-detail', pk=game.pk)

    context = {
        'form': form,
    }

    return render(request, 'games/game_form.html', context)

def game_delete(request, pk):
    game = Game.objects.get(pk=pk)

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
    genre = Genre.objects.get(pk=pk)

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
    genre = Genre.objects.get(pk=pk)
    form = GenreForm(request.POST or None, instance=genre)

    if form.is_valid():
        form.save()
        return redirect('genre-detail', pk=genre.pk)

    context = {
        'form': form,
    }

    return render(request, 'genres/genre_form.html', context)


def genre_delete(request, pk):
    genre = Genre.objects.get(pk=pk)

    if request.method == 'POST':
        genre.delete()
        return redirect('genre-list')

    context = {
        'genre': genre,
    }

    return render(request, 'genres/genre_confirm_delete.html', context)