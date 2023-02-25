from django.shortcuts import render
from .models import Menu

# Create your views here.


def index(request):
    all_menus = Menu.objects.all()
    return render(request, 'index.html', {'all_menus': all_menus})


def menu_item(request, menu_name, level, left, right):
    return render(request, 'menu_item.html', {'menu_name': menu_name,
                                              'level': level,
                                              'left': left,
                                              'right': right,
                                              })