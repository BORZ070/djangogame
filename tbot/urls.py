from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from account.views import index_views
from tbot.bot import set_webhook, telegram_webhook
from tbot.views import tlink_views



urlpatterns = [
    path('set-webhook/', set_webhook, name='set_webhook'),
    path('webhook/', telegram_webhook, name='telegram_webhook'),
    path('telegram', tlink_views, name='tlink')

]