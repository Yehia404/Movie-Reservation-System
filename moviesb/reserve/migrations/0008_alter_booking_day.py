# Generated by Django 4.2.1 on 2023-05-16 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0007_booking_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Day',
            field=models.CharField(max_length=9),
        ),
    ]
