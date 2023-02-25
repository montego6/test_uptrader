from django import template
from django.db.models import Q
from ..models import MenuItem

register = template.Library()


@register.filter(name='indent')
def indent_string(value, num_tabs=1):
    return ' ' * 4 * num_tabs + value


@register.inclusion_tag('menu.html')
def draw_menu(menu_name, *args):
    menu_items = MenuItem.objects.select_related('menu')\
        .filter(menu__name=menu_name, level__lte=1).order_by('left')
    if args:
        left, right = [*args]
        menu_items = MenuItem.objects.select_related('menu') \
            .filter(menu__name=menu_name) \
            .filter(Q(parent__left__lte=left, parent__right__gte=right) |
                    Q(level=0)).order_by('left')
    return {'menu_items': menu_items}
