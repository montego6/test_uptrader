from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.urls import reverse
from .funcs import mptt
# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
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

    def get_absolute_url(self):
        return reverse('menu-item', kwargs={'menu_name': self.menu.name,
                                            'level': self.level,
                                            'left': self.left,
                                            'right': self.right,
                                            })

    def __str__(self):
        parent = f' - child of {self.parent.name}' if self.parent else ''
        return f'{self.menu.name} - {self.name}' + parent


@receiver(post_delete)
def delete_menu_item(sender, instance, **kwargs):
    if sender == MenuItem:
        recalculate_mptt(instance)


@receiver(post_save)
def save_menu_item(sender, instance, **kwargs):
    if sender == MenuItem:
        recalculate_mptt(instance)


def recalculate_mptt(instance):
    main_node = MenuItem.objects.get(menu__name=instance.menu.name, level=0)
    node_list = []
    mptt(main_node, 0, node_list, 0)
    MenuItem.objects.bulk_update(node_list, ['left', 'right', 'level'])
