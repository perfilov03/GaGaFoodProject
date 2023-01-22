from django.contrib import admin
from restaurant.models import *
from .models import *
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin


class RestaurantsAdmin (ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'logo')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('category',)
    list_filter = ('id', 'title', 'category')


class RestInine(admin.TabularInline):
    model = Restaurants


class CategoryAdmin (ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    inlines = [RestInine, ]


admin.site.register(Restaurants, RestaurantsAdmin)
admin.site.register(Category, CategoryAdmin)
