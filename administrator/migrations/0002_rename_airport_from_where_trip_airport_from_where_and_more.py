# Generated by Django 4.1 on 2022-08-29 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administrator", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="trip",
            old_name="Airport_from_where",
            new_name="airport_from_where",
        ),
        migrations.AddField(
            model_name="hotel",
            name="standart",
            field=models.IntegerField(null=True),
        ),
    ]
