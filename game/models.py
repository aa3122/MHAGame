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




class Organization(models.Model):
    org_id = models.AutoField(db_column='org_ID', primary_key=True)  # Field name made lowercase.
    org_name = models.CharField(db_column='org_Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'organization'


class Session(models.Model):
    sessionid = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Game, models.DO_NOTHING, db_column='gameid')
    student = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
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
