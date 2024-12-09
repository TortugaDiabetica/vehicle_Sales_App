from django import forms
from .models import Vehicle


class VehicleCreateForm(forms.ModelForm):
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
            "price",
            "mileage",
            "location",
            "image",
            "description",
        ]

        labels = {
            "brand": "Marca",
            "model": "Modelo",
            "year": "Año",
            "color": "Color",
            "vehicle_type": "Tipo de vehículo",
            "seat_number": "Número de asientos",
            "transmission": "Transmisión",
            "fuel_type": "Tipo de combustible",
            "price": "Precio de venta",
            "mileage": "Kilometraje",
            "location": "Sucursal",
            "image": "Imagen",
            "description": "Descripción",
        }

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 0:
            raise forms.ValidationError("El precio debe ser mayor a 0.")
        return price


class VehicleUpdateForm(forms.ModelForm):
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
            "price",
            "sale_status",
            "mileage",
            "location",
            "image",
            "description",
        ]

        labels = {
            "brand": "Marca",
            "model": "Modelo",
            "year": "Año",
            "color": "Color",
            "vehicle_type": "Tipo",
            "seat_number": "Número de asientos",
            "transmission": "Transmisión",
            "fuel_type": "Tipo de combustible",
            "price": "Precio de venta",
            "sale_status": "Estado de venta",
            "mileage": "Kilometraje",
            "location": "Sucursal",
            "image": "Imagen",
            "description": "Descripción",
        }

        widgets = {
            "available_from": forms.DateInput(attrs={"type": "date"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        sale_status = cleaned_data.get("sale_status")
        original_status = self.instance.sale_status

        # Validaciones de cambio de estado
        if original_status == "SOLD" and sale_status != "SOLD":
            raise forms.ValidationError(
                "No se puede cambiar el estado de un vehículo vendido."
            )

        return cleaned_data
