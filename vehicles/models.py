from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MinValueValidator


# Se crea el modelo Vehicle con los campos necesarios para almacenar la información de un vehículo
class Vehicle(models.Model):
    # Información básica del vehiculo:
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=30)
    vehicle_type_choices = [
        ("Sedan", "Sedán"),
        ("SUV", "SUV"),
        ("Hatchback", "Hatchback"),
        ("Coupe", "Coupé"),
        ("Convertible", "Convertible"),
        ("Wagon", "Wagon"),
        ("Truck", "Camioneta"),
        ("Van", "Furgoneta"),
        ("Minivan", "Miniván"),
        ("Motorcycle", "Motocicleta"),
        ("Electric", "Eléctrico"),
        ("Hybrid", "Híbrido"),
        ("Luxury", "De lujo"),
        ("Sports", "Deportivo"),
        ("Pickup", "Pickup"),
    ]  # Se define una lista de tuplas con las opciones de tipo de vehículo para el campo vehicle_type

    vehicle_type = models.CharField(
        max_length=20,
        null=True,
        choices=vehicle_type_choices,
    )

    seat_number = models.PositiveIntegerField()  # Número de asientos

    transmission = models.CharField(
        max_length=20,
        choices=[
            ("Automatic", "Automatico"),
            ("Manual", "Manual"),
        ],
    )

    fuel_type = models.CharField(
        max_length=20,
        choices=[
            ("Gasoline", "Gasolina"),
            ("Diesel", "Diesel"),
            ("Electric", "Electrico"),
            ("Hybrid", "Hibrido"),
        ],
    )

    daily_rate = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(0)]
    )  # Tarifa diaria del vehículo en pesos chilenos

    isAvaiable = [
        ("No", "No"),
        ("Si", "Si"),
    ]
    available = models.CharField(
        choices=isAvaiable,
        null=False,
        max_length=20,
    )  # Disponibilidad del vehículo
    mileage = models.PositiveIntegerField()  # Kilometraje del vehículo

    available_from = models.DateField(
        null=True, blank=True, default=timezone.now
    )  # Fecha de disponibilidad del vehículo

    location_choices = [
        ("Iquique", "Iquique"),
        ("Valparaíso", "Valparaíso"),
        ("Santiago", "Santiago"),
    ]
    location = models.CharField(
        choices=location_choices,
        null=False,
        max_length=50,
    )  # Nombre de la ubicación de la sucursal

    # Imagen y descripción del vehículo:
    image = models.ImageField(upload_to="vehicles/", null=True, blank=True)
    description = models.TextField(blank=True)

    def formatted_daily_rate(self):
        return f"${self.daily_rate:,.0f}".replace(",", ".") + " CLP"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
