# Generated by Django 3.2 on 2021-05-23 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0002_auto_20210523_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='instructor',
        ),
        migrations.AddField(
            model_name='coursesection',
            name='instructor',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instructor', to=settings.AUTH_USER_MODEL),
        ),
    ]