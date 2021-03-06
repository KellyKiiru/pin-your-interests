# Generated by Django 4.0.4 on 2022-05-28 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_categories_image_remove_pin_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin_name', models.CharField(max_length=30)),
                ('pin_description', models.TextField()),
                ('pin_image', models.ImageField(unique=True, upload_to='pins/')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
            options={
                'ordering': ['pin_name'],
            },
        ),
        migrations.RemoveField(
            model_name='image',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='image',
            name='location',
        ),
        migrations.RemoveField(
            model_name='location',
            name='name',
        ),
        migrations.AddField(
            model_name='location',
            name='location',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='categories',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='pin',
            name='pin_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.location'),
        ),
    ]
