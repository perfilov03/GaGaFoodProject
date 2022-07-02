from django.contrib import admin
from .models import *


class CouponsAdmin (admin.ModelAdmin):
    list_display = ('code', 'percent', 'title')
    list_display_links = ('code', 'title')
    search_fields = ('code', 'title',)
    list_editable = ('percent',)
    list_filter = ('percent', 'title', )


admin.site.register(Coupons, CouponsAdmin)
