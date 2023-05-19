# Generated by Django 4.2.1 on 2023-05-18 19:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0008_alter_booking_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=11, validators=[django.core.validators.MinLengthValidator(11)])),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]