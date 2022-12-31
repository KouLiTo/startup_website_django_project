from django import template


register = template.Library()


@register.filter(name="round_value")
def round_value(value: float) -> float:
    return round(value, 2)
