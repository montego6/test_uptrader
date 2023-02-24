from django import template
from django.db.models import Q
from ..models import Menu, MenuItem

register = template.Library()


@register.filter(name='indent')
def indent_string(value, num_tabs=1):
    return ' '*4*num_tabs + value


@register.inclusion_tag('menu.html')
def draw_menu(menu_name, *args):
    menu_items = MenuItem.objects.filter(menu__name=menu_name, level__lte=1).order_by('id')
    if args:
        level, left, right, parent_left, parent_right = [*args]
        menu_items = MenuItem.objects.select_related('menu')\
                                             .filter(menu__name=menu_name)\
                                             .filter(Q(left__lte=left, right__gte=right) |
                                             Q(left__gt=parent_left, right__lt=parent_right, level=level) |
                                             Q(left__gt=left, right__lt=right, level=level+1) |
                                             Q(level=1) |
                                             Q(level__lt=level, parent_left__lt=left, parent_right__gt=right)
                                             ).order_by('left')
    return {'menu_items': menu_items}