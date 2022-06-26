from django.contrib import admin

from dish.models import *


class DishAdmin (admin.ModelAdmin):
    list_display = ('id', 'title', 'restaurant', 'price', 'cover')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('restaurant', 'price')
    list_filter = ('id', 'title', 'restaurant', 'price')


admin.site.register(Dish, DishAdmin)
