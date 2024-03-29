# Generated by Django 3.2 on 2021-07-08 02:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_game_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='initial_budget_currency',
        ),
        migrations.AlterField(
            model_name='game',
            name='initial_budget',
            field=models.DecimalField(decimal_places=2, default=150000000, max_digits=14, validators=[django.core.validators.MinValueValidator(150000000)]),
        ),
    ]
