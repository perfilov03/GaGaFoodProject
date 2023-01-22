from django.contrib import admin
from dish.models import *
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin


class DishAdmin (ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('id', 'title', 'restaurant', 'price', 'cover')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('restaurant', 'price')
    list_filter = ('id', 'title', 'restaurant', 'price')


admin.site.register(Dish, DishAdmin)
