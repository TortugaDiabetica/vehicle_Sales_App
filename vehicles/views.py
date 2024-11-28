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


class VehicleListView(ListView):
    model = Vehicle
    template_name = "vehicles_list.html"
    context_object_name = "vehicles"


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


class CreateVehicle(CreateView):
    model = Vehicle
    template_name = "vehicle_create.html"
    form_class = FormCreateVehicle  # Se define el formulario que se utilizará para la creación de vehículos
    success_url = reverse_lazy(
        "vehicles:vehicles_list"
    )  # Añadido para redirigir después de crear
