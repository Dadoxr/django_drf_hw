# Generated by Django 4.2.7 on 2023-11-22 15:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edu", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="preview_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="lesson/", verbose_name="превью"
            ),
        ),
    ]
