from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from games.models import Game


class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1,
                              message='Score cannot be lower than 1.'),
            MaxValueValidator(100,
                              message='Score cannot be higher than 100.'),
        ]
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.game} - {self.rating}"


