from django.contrib import admin
from authentication.models import *


class UserAdmin (admin.ModelAdmin):
    list_display = ('id', 'email', 'telephone')
    list_display_links = ('id', 'email', 'telephone')
    search_fields = ('email', 'telephone', )


admin.site.register(User, UserAdmin)
