# Generated by Django 4.1.3 on 2023-03-06 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("salones", "0003_remove_parametros_imagenes_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parametros_imagenes",
            name="image",
            field=models.ImageField(upload_to="images/"),
        ),
    ]
