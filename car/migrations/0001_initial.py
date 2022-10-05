# Generated by Django 4.1.1 on 2022-10-05 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=20)),
                ('car_model', models.CharField(max_length=20)),
                ('daily_price', models.CharField(max_length=20)),
                ('is_available', models.BooleanField()),
                ('place_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_start_date', models.DateTimeField()),
                ('rent_end_date', models.DateTimeField()),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='car.car')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
