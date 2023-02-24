from django import template
from django.db.models import Q
from ..models import Menu, MenuItem

register = template.Library()


@register.filter(name='indent')
def indent_string(value, num_tabs=1):
    return ' '*4*num_tabs + value


@register.inclusion_tag('menu.html')
def draw_menu(menu_name, *args):
    menu = Menu.objects.get(name=menu_name)
    menu_items = MenuItem.objects.filter(menu=menu, level__lte=1).order_by('id')
    if args:
        level, left, right = [*args]
        menu_items = MenuItem.objects.filter(Q(left__lte=left, right__gte=right) |
                                             Q(left__gt=left, right__gt=right) |
                                             Q(left__gt=left, level=level+1)
                                             )
    return {'menu_items': menu_items}