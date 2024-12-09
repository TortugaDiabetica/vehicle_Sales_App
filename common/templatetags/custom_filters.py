from django.contrib.auth.models import Group
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return int(value) * int(arg)

@register.filter
def add(value, arg):
    return int(value) + int(arg)

@register.filter(name="has_group")
def has_group(user, group_name):
    try:
        group = Group.objects.get(name=group_name)
        return group in user.groups.all()
    except Group.DoesNotExist:
        return False

@register.filter(name='add_class')
def add_class(field, css_class):
    """
    Adds a CSS class to a form field.
    Usage: {{ form.field|add_class:"my-class" }}
    """
    return field.as_widget(attrs={"class": css_class})