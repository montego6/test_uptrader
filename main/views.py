from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def menu_item(request, menu_name, level, left, right, parent_left, parent_right):
    return render(request, 'menu_item.html', {'menu_name': menu_name,
                                              'level': level,
                                              'left': left,
                                              'right': right,
                                              'parent_left': parent_left,
                                              'parent_right': parent_right
                                              })