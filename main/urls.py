from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:menu_name>/<int:level>-<int:left>-<int:right>/', views.menu_item, name='menu-item'),
]