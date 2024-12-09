import django_filters
from .models import Vehicle
from django import forms


class VehicleFilter(django_filters.FilterSet):
    price__lte = django_filters.NumberFilter(
        field_name="price",
        lookup_expr="lte",
        label="Precio máximo",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )

    price__gte = django_filters.NumberFilter(
        field_name="price",
        lookup_expr="gte",
        label="Precio mínimo",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )

    vehicle_type = django_filters.ChoiceFilter(
        choices=Vehicle.vehicle_type_choices,
        label="Tipo de vehículo",
        empty_label="Todos los tipos",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    sale_status = django_filters.ChoiceFilter(
        choices=Vehicle.SALE_STATUS,
        label="Estado",
        empty_label="Todos los estados",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    location = django_filters.ChoiceFilter(
        choices=Vehicle.location_choices,
        label="Ubicación",
        empty_label="Todas las ubicaciones",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    year__gte = django_filters.NumberFilter(
        field_name="year",
        lookup_expr="gte",
        label="Año desde",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )

    transmission = django_filters.ChoiceFilter(
        choices=[
            ("Automatic", "Automático"),
            ("Manual", "Manual"),
        ],
        label="Transmisión",
        empty_label="Todas",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    ordering = django_filters.OrderingFilter(
        choices=(
            ("sale_date", "Fecha de venta"),
            ("price", "Precio menor"),
            ("-price", "Precio mayor"),
        ),
        label="Ordenar por",
    )

    class Meta:
        model = Vehicle
        fields = [
            "vehicle_type",
            "sale_status",
            "location",
            "transmission",
            "price__lte",
            "price__gte",
            "year__gte",
            "ordering",
        ]
