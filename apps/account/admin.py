from django.contrib import admin
from account.models import Profile


@admin.register(Profile)
class profile_admin(admin.ModelAdmin):
    readonly_fields = ['uuid']
    list_display = ['id', 'user', 'uuid']

