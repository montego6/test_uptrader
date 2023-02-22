from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def menu_item(request, menu_name, id):
    return render(request, 'menu_item.html', {'menu_name': menu_name, 'id': id})