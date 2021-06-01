# Generated by Django 3.2 on 2021-05-24 23:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game', models.AutoField(primary_key=True, serialize=False)),
                ('join_tag', models.CharField(default=1, max_length=100, unique=True)),
                ('game_name', models.CharField(db_column='game_name', max_length=100)),
                ('initial_population', models.IntegerField(default=0)),
                ('initial_budget', models.DecimalField(decimal_places=2, default=0, max_digits=13)),
                ('Instructor', models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'game',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session', models.AutoField(primary_key=True, serialize=False)),
                ('immunization_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('EDUSmoking_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('EDUDisease_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('Screening_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('TestingLab_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('TestingPharmo_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('AnnualPCP_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('HospitalCare_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('MentalHealth_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('EmergencyCare_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('OutPatientSurg_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('OutPatientRadio_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('PhysicianPCP_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('PhysicianSpec_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('UrgentCare_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('HomeHealth_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('Hospice_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('LTAC_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('SkilledNursing_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('NursingHome_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('AsstLiving_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('IndLiving_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('NameBrand_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('GenDrugs_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('SpecialtyDrugs_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('DurableMedEqu_perc', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5)),
                ('TobTax_perc', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5)),
                ('Alcohol_perc', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5)),
                ('FattyFoods_perc', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5)),
                ('SugFoods_perc', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5)),
                ('game_tag', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='game.game')),
                ('student', models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'session',
                'managed': True,
            },
        ),
    ]
