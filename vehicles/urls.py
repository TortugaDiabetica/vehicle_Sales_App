from django.urls import path
from .views import (
    VehicleDetailView,
    VehicleListView,
    DeleteVehicle,
    UpdateVehicle,
    CreateVehicle,
)
from django.conf import settings
from django.conf.urls.static import static

app_name = "vehicles"

urlpatterns = [
    path("", VehicleListView.as_view(), name="vehicles_list"),
    path("vehicle/<int:pk>/", VehicleDetailView.as_view(), name="vehicle_details"),
    path("vehicle/<int:pk>/delete/", DeleteVehicle.as_view(), name="vehicle_delete"),
    path("vehicle/<int:pk>/update/", UpdateVehicle.as_view(), name="vehicle_update"),
    path("vehicle/create/", CreateVehicle.as_view(), name="vehicle_create"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
