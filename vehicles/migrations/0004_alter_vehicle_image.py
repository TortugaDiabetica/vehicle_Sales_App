# Generated by Django 5.1.3 on 2024-11-12 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_vehicle_vehicle_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='vehicles/'),
        ),
    ]
