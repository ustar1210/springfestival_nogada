# Generated by Django 4.2.1 on 2023-05-16 15:38

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notice", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="notificationimage",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to=core.models.image_upload_path
            ),
        ),
    ]
