from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="NitFood API",
        default_version="v1",
        description="API Endpoints for NitFood.",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path(
        "api/v1/",
        include(
            [
                path("auth/", include("accounts.urls")),
                path("product/", include("product.urls")),
            ]
        ),
    ),
]
