# Generated by Django 5.0.1 on 2024-02-03 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_carinventory_alter_car_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]