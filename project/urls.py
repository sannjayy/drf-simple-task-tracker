from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Task Tracker",
      default_version='v0.0',
      description="Simple Task Tracker Application",
      terms_of_service="https://www.domain.com/",
      contact=openapi.Contact(email="info@example.in"),
      license=openapi.License(name="All right reserved."),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/v1/', include('app_accounts.urls')),

    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.ENV_NAME != 'prod':
    urlpatterns += [
        path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('api/api.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
    ]