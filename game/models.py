from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Game(models.Model):
    instructor = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    game_name = models.CharField(db_column='game_name', max_length=100)
    initial_population = models.IntegerField(blank=True, null=True)
    initial_budget = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game'

    def __str__(self):
        int_game = '%i' % (self.id)
        return 'Game {}'.format(int_game)

class Session(models.Model):
    sessionid = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    immunization_perc = models.IntegerField(blank=True, null=False)
    EDUSmoking_perc = models.IntegerField(blank=True, null=False)
    EDUDisease_perc = models.IntegerField(blank=True, null=False)
    Screening_perc = models.IntegerField(blank=True, null=False)
    TestingLab_perc = models.IntegerField(blank=True, null=False)
    AnnualPCP_perc = models.IntegerField(blank=True, null=False)
    HospitalCare_perc = models.IntegerField(blank=True, null=False)
    MentalHealth_perc = models.IntegerField(blank=True, null=False)
    EmergencyCare_perc = models.IntegerField(blank=True, null=False)
    OutPatientSurg_perc = models.IntegerField(blank=True, null=False)
    OutPatientRadio_perc = models.IntegerField(blank=True, null=False)
    PhysicianPCP_perc = models.IntegerField(blank=True, null=False)
    PhysicianSpec_perc = models.IntegerField(blank=True, null=False)
    UrgentCare_perc = models.IntegerField(blank=True, null=False)
    HomeHealth_perc = models.IntegerField(blank=True, null=False)
    Hospice_perc = models.IntegerField(blank=True, null=False)
    LTAC_perc = models.IntegerField(blank=True, null=False)
    SkilledNursing_perc = models.IntegerField(blank=True, null=False)
    NursingHome_perc = models.IntegerField(blank=True, null=False)
    AsstLiving_perc = models.IntegerField(blank=True, null=False)
    IndLiving_perc = models.IntegerField(blank=True, null=False)
    NameBrand_perc = models.IntegerField(blank=True, null=False)
    GenDrugs_perc = models.IntegerField(blank=True, null=False)
    SpecialtyDrugs_perc = models.IntegerField(blank=True, null=False)
    DurableMedEqu_perc = models.IntegerField(blank=True, null=False)
    TobTax_perc = models.IntegerField(blank=True, null=False)
    Alcohol_perc = models.IntegerField(blank=True, null=False)
    FattyFoods_perc = models.IntegerField(blank=True, null=False)
    SugFoods_perc = models.IntegerField(blank=True, null=False)
    immunization_perc = models.IntegerField(blank=True, null=False)
    immunization_perc = models.IntegerField(blank=True, null=False)
    prev_expenses = models.IntegerField(blank=True, null=True)
    acute_expenses = models.IntegerField(blank=True, null=True)
    ambul_expenses = models.IntegerField(blank=True, null=True)
    long_expenses = models.IntegerField(blank=True, null=True)
    pharm_expenses = models.IntegerField(blank=True, null=True)
    tax_total = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'session'

    def __str__(self):
        session_num = '%i' % (self.sessionid)
        return 'Session {}'.format(session_num)

class CourseSection(models.Model):
    crn = models.IntegerField()
    title = models.CharField(max_length=100)
    term = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    prefix = models.CharField(max_length=40)
    credit_hours = models.IntegerField()
    course_num = models.CharField(max_length=40)
    section_num = models.CharField(max_length=40)
    email = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_section'
