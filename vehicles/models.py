from django.db import models
from django.utils import timezone


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
            ("Automatic", "Automatic"),
            ("Manual", "Manual"),
        ],
    )

    fuel_type = models.CharField(
        max_length=20,
        choices=[
            ("Gasoline", "Gasoline"),
            ("Diesel", "Diesel"),
            ("Electric", "Electric"),
            ("Hybrid", "Hybrid"),
        ],
    )

    daily_rate = models.DecimalField(
        max_digits=8, decimal_places=2
    )  # Tarifa diaria del vehículo en pesos chilenos

    available = models.BooleanField(default=True)  # Disponibilidad del vehículo
    isAvaiable = [("Yes", "No")]
    mileage = models.PositiveIntegerField()  # Kilometraje del vehículo

    available_from = models.DateField(
        null=True, blank=True, default=timezone.now
    )  # Fecha de disponibilidad del vehículo

    location = models.CharField(max_length=100)  # Nombre de la ubicación de la sucursal

    # Imagen y descripción del vehículo:
    image = models.ImageField(upload_to="vehicles/", null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
