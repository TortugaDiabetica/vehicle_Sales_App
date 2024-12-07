# Generated by Django 5.1.3 on 2024-12-07 18:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0012_alter_vehicle_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='daily_rate',
            field=models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]