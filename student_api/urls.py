
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import permissions
from django.contrib.auth import views as auth_views
from .views import greet_view
from rest_framework.permissions import AllowAny
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(openapi.Info(
    title = "Students API",
    default_version = "v1",
    description = "API for managing student data, including attendance, subjects",
    contact = openapi.Contact(email="cheruiyotevans646@gmail.com"),
    license = openapi.License(name="BSD License"),
    ),
    public= True,
    permission_classes = (AllowAny,)  # AllowAny permission for public access to the schema,
)

urlpatterns = [
    path('', lambda request: redirect('swagger/')),
    path('admin/', admin.site.urls),
    path("", include('students.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('api-token-auth/', obtain_auth_token),
    path("greet/", greet_view, name='greet'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

