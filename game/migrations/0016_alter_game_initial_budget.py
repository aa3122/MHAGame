# Generated by Django 3.2 on 2021-07-08 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0015_alter_game_initial_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='initial_budget',
            field=models.IntegerField(default=0),
        ),
    ]
