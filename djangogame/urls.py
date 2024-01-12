from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from account.views import index_views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken import views as api_auth_views

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', index_views, name='index_page'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('summernote/', include('django_summernote.urls')),
    path('article/', include('articles.urls')),
    path('games/', include('games.urls')),
    path('api/', include('api.urls')),
    #swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api-token-auth/', api_auth_views.obtain_auth_token),
    #TG
    path('tbot/', include('tbot.urls')),
    #blog
    path('blog', include('blog.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

