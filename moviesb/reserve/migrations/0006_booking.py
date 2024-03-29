# Generated by Django 4.2.1 on 2023-05-16 18:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0005_alter_seat_seatno'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=7, validators=[django.core.validators.MinLengthValidator(7)])),
                ('Customer', models.ManyToManyField(blank=True, null=True, to='reserve.customer')),
                ('Movie', models.ManyToManyField(blank=True, null=True, to='reserve.movie')),
            ],
        ),
    ]
