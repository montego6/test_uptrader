from django.contrib import admin
from .models import Menu, MenuItem
# Register your models here.


class MenuItemAdmin(admin.ModelAdmin):
    list_select_related = ['menu', 'parent']
    readonly_fields = ['left', 'right', 'level', 'parent_left', 'parent_right']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parent":
            kwargs["queryset"] = MenuItem.objects.select_related('parent', 'menu')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Menu)
admin.site.register(MenuItem, MenuItemAdmin)


