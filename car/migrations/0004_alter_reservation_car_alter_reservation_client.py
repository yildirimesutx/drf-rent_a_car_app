# Generated by Django 4.1.1 on 2022-10-04 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car', '0003_alter_reservation_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='car.car'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
