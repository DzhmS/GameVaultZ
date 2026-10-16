from django import template

register = template.Library()


@register.filter
def score_label(value):
    if value >= 90:
        return 'Excellent'
    elif value >= 75:
        return 'Very Good'
    elif value >= 60:
        return 'Good'
    elif value >= 40:
        return 'Average'

    return 'Poor'