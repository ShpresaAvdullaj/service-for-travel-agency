# Generated by Django 4.1 on 2022-09-21 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("administrator", "0003_alter_purchaseofatrip_trip"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trip",
            name="number_of_days",
        ),
    ]