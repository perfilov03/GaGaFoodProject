from django.contrib import admin
from authentication.models import *
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin


class UserAdmin (ImportExportModelAdmin, SimpleHistoryAdmin,admin.ModelAdmin):
    list_display = ('id', 'email', 'telephone')
    list_display_links = ('id', 'email', 'telephone')
    search_fields = ('email', 'telephone', )


admin.site.register(User, UserAdmin)
