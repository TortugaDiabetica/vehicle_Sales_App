from .models import Vehicle
from django import forms


# Formulario para actualizar la información de los vehículos en el sistema
class FormUpdateVehicle(forms.ModelForm):
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
        ]  # Se definen los campos que se mostrarán en el formulario de actualización

        labels = {
            "brand": "Marca",
            "model": "Modelo",
            "year": "Año",
            "color": "Color",
            "vehicle_type": "Tipo",
            "seat_number": "Número de asientos",
            "transmission": "Transmisión",
            "fuel_type": "Tipo de combustible",
            "daily_rate": "Tarifa diaria",
            "available": "Disponible",
            "mileage": "Kilometraje",
            "available_from": "Disponible desde",
            "location": "Sucursal",
            "image": "Imagen",
            "description": "Descripción",
        }  # Se definen las etiquetas de los campos del formulario de actualización de vehículos

        widgets = {
            "available_from": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_daily_rate(self):
        daily_rate = self.cleaned_data.get("daily_rate")
        if daily_rate < 0:
            raise forms.ValidationError("El precio diario no puede ser negativo.")
        return daily_rate


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
            "location": "Sucursal",
            "image": "Imagen",
            "description": "Descripción",
        }

        widgets = {
            "available_from": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_daily_rate(self):
        daily_rate = self.cleaned_data.get("daily_rate")
        if daily_rate < 0:
            raise forms.ValidationError("El precio diario no puede ser negativo.")
        return daily_rate
