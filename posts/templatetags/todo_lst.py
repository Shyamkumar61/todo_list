from django import template

register = template.Library()

@register.filter(name="upp")
def upp(value):
    return value.upper()

@register.filter(name="capital")
def capital(value):
    return value.capitalize()