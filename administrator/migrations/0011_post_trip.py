# Generated by Django 4.1 on 2022-10-24 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("administrator", "0010_post_like"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="trip",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="trip_post",
                to="administrator.trip",
            ),
        ),
    ]
