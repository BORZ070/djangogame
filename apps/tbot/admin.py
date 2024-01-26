from django.contrib import admin

from tbot.models import TbotUserProfile, SupportQ, TSpam, WebhookLink

admin.site.register(TbotUserProfile)
admin.site.register(SupportQ)
admin.site.register(TSpam)
admin.site.register(WebhookLink)

