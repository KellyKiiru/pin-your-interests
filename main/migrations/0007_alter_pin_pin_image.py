# Generated by Django 4.0.4 on 2022-05-30 07:04

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_pin_location_pin_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='pin_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='images'),
        ),
    ]
