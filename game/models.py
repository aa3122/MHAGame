from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Game(models.Model):
    game = models.AutoField(primary_key=True)
    join_tag = models.CharField(default=1, max_length=100, unique=True)
    Instructor = models.ForeignKey(User,null=True, on_delete=models.CASCADE, limit_choices_to={'is_staff': True},)
    game_name = models.CharField(db_column='game_name', max_length=100)
    initial_population = models.IntegerField(blank=False, null=False, default=0)
    initial_budget = models.DecimalField(max_digits = 13, decimal_places = 2, blank=False, null=False, default=0)
    course  = models.CharField(max_length = 240, null=True)

    class Meta:
        managed = True
        db_table = 'game'

    def __str__(self):
        return self.join_tag

class Session(models.Model):
    session = models.AutoField(primary_key=True)
    game_tag = models.ForeignKey(Game, default=1, on_delete=models.CASCADE, related_name='hostgame')
    student = models.ForeignKey(User, null=True, on_delete=models.CASCADE, limit_choices_to={'is_staff': False},)
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
    TobTax_perc = models.IntegerField(blank=True, null=False, default=0)
    DurableMedEqu_perc = models.IntegerField(blank=True, null=False, default=100)
    TobTax_perc = models.DecimalField(max_digits = 5, decimal_places = 1, blank=True, null=False, default=0)
    Alcohol_perc = models.DecimalField(max_digits = 5, decimal_places = 1, blank=True, null=False, default=0)
    FattyFoods_perc = models.DecimalField(max_digits = 5, decimal_places = 1,blank=True, null=False, default=0)
    SugFoods_perc = models.DecimalField(max_digits = 5, decimal_places = 1, blank=True, null=False, default=0)
    
    class Meta:
        managed = True
        db_table = 'session'

    def __str__(self):
        session_num = '%i' % (self.session)
        return 'Session {}'.format(session_num)