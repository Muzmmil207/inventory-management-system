from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.dashboard.urls")),
    path("stock/", include("apps.stock.urls")),
    path("users/", include("apps.users.urls")),
    # Third part app
    path("__debug__/", include("debug_toolbar.urls")),
]
