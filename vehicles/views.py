from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Vehicle
from django.urls import reverse_lazy
from .forms import FormUpdateVehicle, FormCreateVehicle
from django.core.exceptions import ValidationError

# Importamos django_filters para aplicar los filtros creados en filters.py a la vistas
from django_filters.views import FilterView
from .filters import VehicleFilter


# Vista que lista vehiculos pero con herencia en los filtros:
class VehicleListView(FilterView):
    model = Vehicle
    template_name = "vehicles_list.html"
    context_object_name = "vehicles"
    filterset_class = VehicleFilter


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
    form_class = FormUpdateVehicle  # Se define el formulario que se utilizará para la actualización de vehículos
    context_object_name = "vehicle"
    success_url = reverse_lazy(
        "vehicles:vehicles_list"
    )  # Añadido para redirigir después de actualizar

    def form_valid(self, form):
        if form.cleaned_data["daily_rate"] < 0:
            form.add_error("daily_rate", "El precio diario no puede ser negativo.")
            return self.form_invalid(form)
        return super().form_valid(form)


class CreateVehicle(CreateView):
    model = Vehicle
    template_name = "vehicle_create.html"
    form_class = FormCreateVehicle  # Se define el formulario que se utilizará para la creación de vehículos
    success_url = reverse_lazy(
        "vehicles:vehicles_list"
    )  # Añadido para redirigir después de crear

    def form_valid(self, form):
        if form.cleaned_data["daily_rate"] < 0:
            form.add_error("daily_rate", "El precio diario no puede ser negativo.")
            return self.form_invalid(form)
        return super().form_valid(form)
