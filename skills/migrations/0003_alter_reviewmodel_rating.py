# Generated by Django 4.2.2 on 2023-06-15 19:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("skills", "0002_remove_skillmodel_price_alter_reviewmodel_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reviewmodel",
            name="rating",
            field=models.PositiveIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ]
            ),
        ),
    ]
