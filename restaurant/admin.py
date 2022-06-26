from django.contrib import admin
from restaurant.models import *
from .models import *


class RestaurantsAdmin (admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'logo')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('category',)
    list_filter = ('id', 'title', 'category')


class CategoryAdmin (admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Restaurants, RestaurantsAdmin)
admin.site.register(Category, CategoryAdmin)
