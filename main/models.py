from django.db import models
from django.urls import reverse
from funcs import mptt
# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        super().save(self, *args, **kwargs)
        MenuItem.objects.create(menu=self, name=self.name, level=0)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    left = models.IntegerField(null=True, blank=True)
    right = models.IntegerField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.level = self.parent.level + 1 if self.parent else 0
        super().save(self, *args, **kwargs)
        main_node = MenuItem.objects.get(level=0)
        mptt(main_node, counter=0)
        MenuItem.objects.bulk_update(MenuItem.objects.all(), ['left', 'right'])

    def get_absolute_url(self):
        return reverse('menu-item', kwargs={'menu_name': self.menu.name, 'id': self.id})

    def __str__(self):
        parent = f' - child of {self.parent.name}' if self.parent else ''
        return f'{self.menu.name} - {self.name}' + parent

