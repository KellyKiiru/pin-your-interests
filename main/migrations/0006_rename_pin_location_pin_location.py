# Generated by Django 4.0.4 on 2022-05-29 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_pin_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pin',
            old_name='pin_location',
            new_name='location',
        ),
    ]