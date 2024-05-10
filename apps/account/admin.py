from django.contrib import admin
from account.models import Profile, ReferralCode


@admin.register(Profile)
class profile_admin(admin.ModelAdmin):
    readonly_fields = ['uuid']
    list_display = ['id', 'user', 'uuid']

@admin.register(ReferralCode)
class CodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'code']

