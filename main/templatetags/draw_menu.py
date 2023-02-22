from django import template
from ..models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('menu.html')
def draw_menu(menu_name, *args):
    menu = Menu.objects.get(name=menu_name)
    menu_items = MenuItem.objects.prefetch_related('children').filter(menu=menu, parent=None).order_by('id')
    ids = []
    if args:
        menu_item = MenuItem.objects.get(id=args[0])
        ids.append(menu_item.id)
        parent = menu_item.parent
        while parent:
            ids.append(parent.id)
            parent = parent.parent
    return {'menu_items': menu_items, 'parent_ids': ids}