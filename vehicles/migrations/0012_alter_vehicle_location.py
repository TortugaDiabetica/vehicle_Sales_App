# Generated by Django 5.1.3 on 2024-12-03 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0011_alter_vehicle_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='location',
            field=models.CharField(choices=[('Iquique', 'Iquique'), ('Valparaíso', 'Valparaíso'), ('Santiago', 'Santiago')], max_length=50),
        ),
    ]
