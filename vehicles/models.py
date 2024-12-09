from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model


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

    price = models.IntegerField(
        validators=[MinValueValidator(0)],
        verbose_name="Precio de venta",
        default=0,
        null=False,
    )  # Cambiado a IntegerField para precios enteros

    SALE_STATUS = [
        ("AVAILABLE", "Disponible"),
        ("RESERVED", "Reservado"),
        ("SOLD", "Vendido"),
    ]

    sale_status = models.CharField(
        max_length=20,
        choices=SALE_STATUS,
        default="AVAILABLE",
        verbose_name="Estado de venta",
    )

    sale_date = models.DateTimeField(null=True, blank=True)

    mileage = models.PositiveIntegerField()  # Kilometraje del vehículo

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

    buyer = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="purchased_vehicles",
    )

    def formatted_price(self):
        """Formato de precio en CLP"""
        return f"${self.price:,.0f}".replace(",", ".") + " CLP"

    def reserve_vehicle(self):
        if self.sale_status == "AVAILABLE":
            self.sale_status = "RESERVED"
            self.save()
            return True
        return False

    def mark_as_sold(self):
        if self.sale_status in ["AVAILABLE", "RESERVED"]:
            self.sale_status = "SOLD"
            self.sale_date = timezone.now()
            self.save()
            return True
        return False

    @property
    def is_available(self):
        return self.sale_status == "AVAILABLE"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    def get_absolute_url(self):
        return reverse("vehicle_details", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-id"]  # Más recientes primero


class TestDrive(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    scheduled_date = models.DateTimeField()
    status_choices = [
        ("SCHEDULED", "Programada"),
        ("COMPLETED", "Completada"),
        ("CANCELLED", "Cancelada"),
    ]
    status = models.CharField(
        max_length=20, choices=status_choices, default="SCHEDULED"
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-scheduled_date"]
