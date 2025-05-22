from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Imports for drf-yasg
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Schema view for swagger/redoc
schema_view = get_schema_view(
    openapi.Info(
        title="BuildSync API",
        default_version='v1',
        description="API documentation for BuildSync project",
        contact=openapi.Contact(email="your@email.com"),  # Replace with your email
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('accounts.urls')),  # Your app endpoints

    # Django REST Framework browsable API login/logout
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Token Authentication (optional, if you still need it alongside JWT)
    # path('api-token-auth/', include('rest_framework.authtoken.urls')),

    # Allauth URLs - separate prefix to avoid conflict
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.account.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),

    # JWT Auth endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger and Redoc UI paths
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
