from django.db import models

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=100)


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children')