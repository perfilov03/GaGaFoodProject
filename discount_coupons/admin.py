from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin


class CouponsAdmin (ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('code', 'percent', 'title')
    list_display_links = ('code', 'title')
    search_fields = ('code', 'title',)
    list_editable = ('percent',)
    list_filter = ('percent', 'title', )


admin.site.register(Coupons, CouponsAdmin)
