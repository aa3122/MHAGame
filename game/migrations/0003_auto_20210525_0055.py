# Generated by Django 3.2 on 2021-05-25 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_alter_session_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='AnnualPCP_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='AsstLiving_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='DurableMedEqu_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='EDUDisease_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='EDUSmoking_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='EmergencyCare_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='GenDrugs_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='HomeHealth_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='Hospice_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='HospitalCare_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='IndLiving_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='LTAC_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='MentalHealth_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='NameBrand_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='NursingHome_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='OutPatientRadio_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='OutPatientSurg_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='PhysicianPCP_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='PhysicianSpec_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='Screening_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='SkilledNursing_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='SpecialtyDrugs_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='TestingLab_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='TestingPharmo_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='UrgentCare_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='immunization_perc',
            field=models.IntegerField(blank=True, default=100),
        ),
    ]