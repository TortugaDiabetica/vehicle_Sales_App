from django.urls import path
from .views import (
    VehicleDetailView,
    VehicleListView,
    DeleteVehicle,
    UpdateVehicle,
    CreateVehicle,
    AdminHistoryView,
    PurchaseVehicle,
    ScheduleTestDrive,
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
    path("admin/history/", AdminHistoryView.as_view(), name="admin_history"),
    path(
        "vehicle/<int:pk>/purchase/",
        PurchaseVehicle.as_view(),
        name="purchase_vehicle",
    ),
    path(
        "vehicle/<int:pk>/schedule-test/",
        ScheduleTestDrive.as_view(),
        name="schedule_test_drive",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
