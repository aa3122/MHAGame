# Generated by Django 3.2 on 2021-07-08 21:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0013_auto_20210708_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='initial_budget',
            field=models.IntegerField(default=500000000, validators=[django.core.validators.MinValueValidator(500000000)]),
        ),
    ]
