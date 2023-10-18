from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from account.views import index_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', index_views, name='index_page'),
    path('social-auth/', include('social_django.urls', namespace='social')),



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

