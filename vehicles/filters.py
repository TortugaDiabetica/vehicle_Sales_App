import django_filters
from .models import Vehicle
from django.forms import NumberInput, Select


class VehicleFilter(django_filters.FilterSet):
    vehicle_type = django_filters.ChoiceFilter(
        choices=[("", "Todos")] + Vehicle.vehicle_type_choices,
        empty_label=None,
        widget=Select(),
    )
    available = django_filters.ChoiceFilter(
        choices=[("", "Disponible")] + Vehicle.isAvaiable,
        empty_label=None,
        widget=Select(),
    )
    daily_rate__lte = django_filters.NumberFilter(
        field_name="daily_rate",
        lookup_expr="lte",
        widget=NumberInput(attrs={"min": "0"}),
        label="Precio máximo",
    )
    daily_rate__gte = django_filters.NumberFilter(
        field_name="daily_rate",
        lookup_expr="gte",
        widget=NumberInput(attrs={"min": "0"}),
        label="Precio mínimo",
    )

    class Meta:
        model = Vehicle
        fields = {
            "vehicle_type": ["exact"],
            "available": ["exact"],
        }
