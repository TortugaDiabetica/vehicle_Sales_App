# Generated by Django 5.1.3 on 2024-11-12 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='type',
        ),
        migrations.DeleteModel(
            name='VehicleType',
        ),
    ]
