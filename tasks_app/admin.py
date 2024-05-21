from django.contrib import admin
from .models import ShopList, ShopListItem, Task

@admin.register(ShopList)
class ShopListAdmin(admin.ModelAdmin):
    pass

@admin.register(ShopListItem)
class ShopListItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'shoplist')
    search_fields = ('name',)
    list_filter = ('shoplist',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_type', 'category')
    search_fields = ('task_type',)
    list_filter = ('task_type', 'category')
