from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:menu_name>/<int:level>-<int:left>-<int:right>-<int:parent_left>-<int:parent_right>/', views.menu_item, name='menu-item'),
]