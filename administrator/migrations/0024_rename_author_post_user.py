# Generated by Django 4.1 on 2022-10-30 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("administrator", "0023_alter_post_author_alter_post_trip"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="author",
            new_name="user",
        ),
    ]
