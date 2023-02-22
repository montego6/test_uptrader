from django import template
from ..models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('menu.html')
def draw_menu(menu_name):
    menu = Menu.objects.get(name=menu_name)
    menu_items = MenuItem.objects.filter(menu=menu, parent=None).order_by('id')
    return {'menu_items': menu_items}