from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['game', 'rating', 'comment']

        labels = {
            'rating': 'Score',
            'comment': 'Review Comment',
        }

        help_texts = {
            'rating': 'Enter a score from 1 to 100.',
            'comment': 'Share your thoughts about the game.',
        }

        widgets = {
            'rating': forms.NumberInput(
                attrs={
                    'placeholder': '1-100',
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'placeholder': 'Write your review here...',
                }
            ),

        }


        error_messages = {
            'rating': {
                'required': 'Please enter a score.',
                'invalid': 'Please enter a valid number.',
            },

        }

