from .models import Vehicle
from django import forms
from django.contrib.auth.models import User


# Formulario para actualizar la información de los vehículos en el sistema
class FormUpdateVehicle(forms.ModelForm):
    class Meta:
        model = Vehicle

        fields = [
            "brand",
            "model",
            "year",
            "color",
            # "vehicle_type_choices",
            "seat_number",
            "transmission",
            "fuel_type",
            "daily_rate",
            "available",
            "mileage",
            "available_from",
            "location",
            "image",
            "description",
        ]  # Se definen los campos que se mostrarán en el formulario de actualización

        labels = {
            "brand": "Marca",
            "model": "Modelo",
            "year": "Año",
            "color": "Color",
            # "vehicle_type_choices": "Tipo",
            "seat_number": "Número de asientos",
            "transmission": "Transmisión",
            "fuel_type": "Tipo de combustible",
            "daily_rate": "Tarifa diaria",
            "available": "Disponible",
            "mileage": "Kilometraje",
            "available_from": "Disponible desde",
            "location": "Ubicación",
            "image": "Imagen",
            "description": "Descripción",
        }  # Se definen las etiquetas de los campos del formulario de actualización de vehículos


# Formulario para la creación de vehículos en el sistema
class FormCreateVehicle(forms.ModelForm):
    class Meta:
        model = Vehicle

        fields = [
            "brand",
            "model",
            "year",
            "color",
            "vehicle_type",
            "seat_number",
            "transmission",
            "fuel_type",
            "daily_rate",
            "available",
            "mileage",
            "available_from",
            "location",
            "image",
            "description",
        ]  # Se definen los campos que se mostrarán en el formulario de creación

        labels = {
            "brand": "Marca",
            "model": "Modelo",
            "year": "Año",
            "color": "Color",
            "vehicle_type": "Tipo de vehículo",
            "seat_number": "Número de asientos",
            "transmission": "Transmisión",
            "fuel_type": "Tipo de combustible",
            "daily_rate": "Tarifa diaria",
            "available": "Disponible",
            "mileage": "Kilometraje",
            "available_from": "Disponible desde",
            "location": "Ubicación",
            "image": "Imagen",
            "description": "Descripción",
        }
