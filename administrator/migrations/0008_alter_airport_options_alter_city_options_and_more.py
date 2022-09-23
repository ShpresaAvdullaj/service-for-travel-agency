# Generated by Django 4.1 on 2022-09-24 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "administrator",
            "0007_alter_trip_options_alter_filterdate_first_date_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="airport",
            options={"permissions": [("addairport", " Add Airport")]},
        ),
        migrations.AlterModelOptions(
            name="city",
            options={"permissions": [("addcity", " Add City")]},
        ),
        migrations.AlterModelOptions(
            name="continent",
            options={"permissions": [("addcontinent", " Add Continent")]},
        ),
        migrations.AlterModelOptions(
            name="country",
            options={"permissions": [("addcountry", " Add Country")]},
        ),
        migrations.AlterModelOptions(
            name="hotel",
            options={"permissions": [("addhotel", " Add Hotel")]},
        ),
    ]
