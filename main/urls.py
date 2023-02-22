from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:menu_name>/<int:id>/', views.menu_item, name='menu-item'),
]