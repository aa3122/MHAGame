# Generated by Django 3.2 on 2021-05-26 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20210525_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='course',
            field=models.CharField(max_length=240, null=True),
        ),
    ]
