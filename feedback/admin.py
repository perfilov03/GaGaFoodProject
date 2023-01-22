from django.contrib import admin
from feedback.models import Feedback
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin


class FeedbackAdmin (ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'telephone')
    search_fields = ('name',)
    list_filter = ('id', 'name', 'telephone')


admin.site.register(Feedback, FeedbackAdmin)
