# Generated by Django 3.2 on 2021-05-22 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='displayusername',
        ),
        migrations.DeleteModel(
            name='AdministrationDisplayusername',
        ),
        migrations.DeleteModel(
            name='AzzaraEvent',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
    ]