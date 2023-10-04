from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import account

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', account.views.index_views, name='index_page'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

