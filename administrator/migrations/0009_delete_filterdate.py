# Generated by Django 4.1 on 2022-09-24 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("administrator", "0008_alter_airport_options_alter_city_options_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="FilterDate",
        ),
    ]
