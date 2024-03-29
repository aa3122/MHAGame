# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#admin app
class AdministrationDisplayusername(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'administration_displayusername'

#admin app
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'

#admin app
class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)

#admin app
class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

#student app
class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

#student app
class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)

#student app
class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

#admin app
class AzzaraEvent(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    classname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'azzara_event'

#game app
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

#admin app
class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'

#admin app
class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)

#admin app
class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

#admin app
class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

#game app
class Game(models.Model):
    instructor = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    initial_population = models.IntegerField(blank=True, null=True)
    initial_budget = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game'

#game app
class Organization(models.Model):
    org_id = models.AutoField(db_column='org_ID', primary_key=True)  # Field name made lowercase.
    org_name = models.CharField(db_column='org_Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'organization'

#game app
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


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    Instructor = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    game_name = models.CharField(db_column='game_name', max_length=100)
    initial_population = models.IntegerField(blank=False, null=False, default=0)
    initial_budget = models.IntegerField(blank=False, null=False, default=0)

    class Meta:
        managed = True
        db_table = 'game'

    def __str__(self):
        int_game = '%i' % (self.id)
        return 'Game {}'.format(int_game)