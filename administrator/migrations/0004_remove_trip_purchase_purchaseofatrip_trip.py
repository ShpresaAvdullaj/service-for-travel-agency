# Generated by Django 4.1 on 2022-09-20 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("administrator", "0003_remove_purchaseofatrip_trip_trip_purchase"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trip",
            name="purchase",
        ),
        migrations.AddField(
            model_name="purchaseofatrip",
            name="trip",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="purchases",
                to="administrator.trip",
                verbose_name="trip",
            ),
        ),
    ]
