from django import forms

from .models import Game, Genre


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'