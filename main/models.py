from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
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
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               related_name='children', null=True, blank=True)
    left = models.IntegerField(null=True, blank=True)
    right = models.IntegerField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)

    def clean(self):
        if self.menu != self.parent.menu:
            raise ValidationError({
                'menu': 'Menu of parent and child should match'})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        kwargs = {'menu_name': self.menu.name,
                  'left': self.left,
                  'right': self.right,
                  }
        return reverse('menu-item', kwargs=kwargs)

    def __str__(self):
        parent = f' - child of {self.parent.name}' if self.parent else ''
        return f'{self.menu.name} - {self.name}' + parent


@receiver([post_save, post_delete], sender=MenuItem)
def save_or_delete_menu_item(sender, instance, **kwargs):
    recalculate_mptt(instance)


def recalculate_mptt(instance):
    main_node = MenuItem.objects.get(menu__name=instance.menu.name, level=0)
    node_list = []
    mptt(main_node, 0, node_list, 0)
    MenuItem.objects.bulk_update(node_list, ['left', 'right', 'level'])
