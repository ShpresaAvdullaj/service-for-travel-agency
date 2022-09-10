# Generated by Django 4.1 on 2022-09-05 20:59

from django.db import migrations, models
import django.db.models.deletion


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
        migrations.AlterField(
            model_name="purchaseofatrip",
            name="trip",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="administrator.trip",
                verbose_name="trip",
            ),
        ),
        migrations.AlterField(
            model_name="trip",
            name="hotel_to_where",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="hotel to where +",
                to="administrator.hotel",
                verbose_name="hotel to where",
            ),
        ),
    ]
