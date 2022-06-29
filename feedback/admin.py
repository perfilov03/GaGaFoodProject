from django.contrib import admin

from feedback.models import Feedback


class FeedbackAdmin (admin.ModelAdmin):
    list_display = ('id', 'name', 'telephone')
    search_fields = ('name',)
    list_filter = ('id', 'name', 'telephone')


admin.site.register(Feedback, FeedbackAdmin)
