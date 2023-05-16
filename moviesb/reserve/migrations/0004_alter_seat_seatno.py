# Generated by Django 4.2.1 on 2023-05-16 18:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0003_seat_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='seatNo',
            field=models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]