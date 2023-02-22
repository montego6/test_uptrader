from django.db import models

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    def get_absolute_url(self):
        return reverse()

    def __str__(self):
        parent = f' - child of {self.parent.name}' if self.parent else ''
        return f'{self.menu.name} - {self.name}' + parent

