from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from .models import Vehicle, TestDrive
from django.urls import reverse_lazy
from .forms import VehicleUpdateForm, VehicleCreateForm

# Importamos django_filters para aplicar los filtros creados en filters.py a la vistas
from django_filters.views import FilterView
from .filters import VehicleFilter
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.views import View
from django.utils import timezone
from django.db.models import Q
from datetime import datetime, timedelta


# Vista que lista vehiculos pero con herencia en los filtros:
class VehicleListView(FilterView):
    model = Vehicle
    template_name = "vehicles_list.html"
    context_object_name = "vehicles"
    filterset_class = VehicleFilter

    def get_queryset(self):
        queryset = Vehicle.objects.all()
        if not self.request.user.is_staff:
            queryset = queryset.filter(sale_status="AVAILABLE")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_staff"] = self.request.user.is_staff
        return context


class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = "vehicle_details.html"
    context_object_name = "vehicle"


class DeleteVehicle(DeleteView):
    model = Vehicle
    template_name = "vehicle_delete.html"
    context_object_name = "vehicle"
    success_url = reverse_lazy("vehicles:vehicles_list")


class UpdateVehicle(UpdateView):
    model = Vehicle
    template_name = "vehicle_update.html"
    form_class = VehicleUpdateForm  # Se define el formulario que se utilizará para la actualización de vehículos
    context_object_name = "vehicle"
    success_url = reverse_lazy(
        "vehicles:vehicles_list"
    )  # Añadido para redirigir después de actualizar

    def form_valid(self, form):
        if form.cleaned_data["price"] < 0:
            form.add_error("price", "El precio del vehiculo no puede ser negativo.")
            return self.form_invalid(form)
        return super().form_valid(form)


class CreateVehicle(CreateView):
    model = Vehicle
    template_name = "vehicle_create.html"
    form_class = VehicleCreateForm  # Se define el formulario que se utilizará para la creación de vehículos
    success_url = reverse_lazy(
        "vehicles:vehicles_list"
    )  # Añadido para redirigir después de crear

    def form_valid(self, form):
        if form.cleaned_data["price"] < 0:
            form.add_error("price", "El precio del vehiculo no puede ser negativo.")
            return self.form_invalid(form)
        return super().form_valid(form)


class AdminHistoryView(UserPassesTestMixin, TemplateView):
    template_name = "admin/vehicle_history.html"

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Filtros para fechas
        date_filter = self.request.GET.get("date_filter", "all")
        today = datetime.now()

        # Query base para vehículos vendidos y reservados
        vehicles_query = Q(sale_status="SOLD") | Q(sale_status="RESERVED")
        filtered_vehicles = Vehicle.objects.filter(vehicles_query)

        # Aplicar filtros de fecha si se seleccionaron
        if date_filter == "today":
            filtered_vehicles = filtered_vehicles.filter(sale_date__date=today.date())
        elif date_filter == "week":
            filtered_vehicles = filtered_vehicles.filter(
                sale_date__gte=today - timedelta(days=7)
            )
        elif date_filter == "month":
            filtered_vehicles = filtered_vehicles.filter(sale_date__month=today.month)

        context.update(
            {
                "vehicles": filtered_vehicles,
                "date_filter": date_filter,
                "total_sold": filtered_vehicles.filter(sale_status="SOLD").count(),
                "total_reserved": filtered_vehicles.filter(
                    sale_status="RESERVED"
                ).count(),
            }
        )
        return context


class PurchaseVehicle(LoginRequiredMixin, View):
    def post(self, request, pk):
        vehicle = get_object_or_404(Vehicle, pk=pk)

        if vehicle.sale_status != "AVAILABLE":
            messages.error(
                request, "Este vehículo ya no está disponible para la venta."
            )
            return redirect("vehicles:vehicle_details", pk=pk)

        vehicle.sale_status = "SOLD"
        vehicle.buyer = request.user
        vehicle.sale_date = timezone.now()
        vehicle.save()

        messages.success(
            request,
            f"¡Felicitaciones! Has comprado el {vehicle.brand} {vehicle.model}.",
        )
        return redirect("vehicles:vehicle_details", pk=pk)

    def get(self, request, pk):
        return self.post(request, pk)


class ScheduleTestDrive(LoginRequiredMixin, CreateView):
    model = TestDrive
    template_name = "vehicles/schedule_test_drive.html"
    fields = ["scheduled_date", "notes"]

    def form_valid(self, form):
        vehicle = get_object_or_404(Vehicle, pk=self.kwargs["pk"])
        form.instance.vehicle = vehicle
        form.instance.customer = self.request.user
        return super().form_valid(form)
