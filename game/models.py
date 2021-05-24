from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Game(models.Model):
    gameid = models.AutoField(primary_key=True)
    join_tag = models.CharField(default=1, max_length=100, unique=True)
    Instructor_id = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    game_name = models.CharField(db_column='game_name', max_length=100)
    initial_population = models.IntegerField(blank=False, null=False, default=0)
    initial_budget = models.IntegerField(blank=False, null=False, default=0)

    class Meta:
        managed = True
        db_table = 'game'

    def __str__(self):
        int_game = '%i' % (self.gameid)
        return 'Game {}'.format(int_game)

class Session(models.Model):
    sessionid = models.AutoField(primary_key=True)
    game_tag = models.ForeignKey(Game, default=1, on_delete=models.CASCADE)
    student = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    immunization_perc = models.IntegerField(blank=True, null=False, default=100)
    EDUSmoking_perc = models.IntegerField(blank=True, null=False, default=100)
    EDUDisease_perc = models.IntegerField(blank=True, null=False, default=100)
    Screening_perc = models.IntegerField(blank=True, null=False, default=100)
    TestingLab_perc = models.IntegerField(blank=True, null=False, default=100)
    TestingPharmo_perc = models.IntegerField(blank=True, null=False, default=100)
    AnnualPCP_perc = models.IntegerField(blank=True, null=False, default=100)
    HospitalCare_perc = models.IntegerField(blank=True, null=False, default=100)
    MentalHealth_perc = models.IntegerField(blank=True, null=False, default=100)
    EmergencyCare_perc = models.IntegerField(blank=True, null=False, default=100)
    OutPatientSurg_perc = models.IntegerField(blank=True, null=False, default=100)
    OutPatientRadio_perc = models.IntegerField(blank=True, null=False, default=100)
    PhysicianPCP_perc = models.IntegerField(blank=True, null=False, default=100)
    PhysicianSpec_perc = models.IntegerField(blank=True, null=False, default=100)
    UrgentCare_perc = models.IntegerField(blank=True, null=False, default=100)
    HomeHealth_perc = models.IntegerField(blank=True, null=False, default=100)
    Hospice_perc = models.IntegerField(blank=True, null=False, default=100)
    LTAC_perc = models.IntegerField(blank=True, null=False, default=100)
    SkilledNursing_perc = models.IntegerField(blank=True, null=False, default=100)
    NursingHome_perc = models.IntegerField(blank=True, null=False, default=100)
    AsstLiving_perc = models.IntegerField(blank=True, null=False, default=100)
    IndLiving_perc = models.IntegerField(blank=True, null=False, default=100)
    NameBrand_perc = models.IntegerField(blank=True, null=False, default=100)
    GenDrugs_perc = models.IntegerField(blank=True, null=False, default=100)
    SpecialtyDrugs_perc = models.IntegerField(blank=True, null=False, default=100)
    DurableMedEqu_perc = models.IntegerField(blank=True, null=False, default=100)
    TobTax_perc = models.IntegerField(blank=True, null=False, default=0)
    Alcohol_perc = models.IntegerField(blank=True, null=False, default=0)
    FattyFoods_perc = models.IntegerField(blank=True, null=False, default=0)
    SugFoods_perc = models.IntegerField(blank=True, null=False, default=0)
    
    class Meta:
        managed = True
        db_table = 'session'

    def __str__(self):
        session_num = '%i' % (self.sessionid)
        return 'Session {}'.format(session_num)