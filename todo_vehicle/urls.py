from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("common.urls"), name=""),
    path("users/", include("users.urls")),
    path("vehicles/", include("vehicles.urls")),
]
