# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Instructor(models.Model):
    inst_email = models.CharField(primary_key=True, max_length=60)
    org = models.ForeignKey('Organization', models.DO_NOTHING, db_column='org_ID')  # Field name made lowercase.
    instructor_fname = models.CharField(max_length=40)
    instructor_lname = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'instructor'


class Organization(models.Model):
    org_id = models.AutoField(db_column='org_ID', primary_key=True)  # Field name made lowercase.
    org_name = models.CharField(db_column='org_Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'organization'


class Student(models.Model):
    stud_email = models.CharField(primary_key=True, max_length=60)
    password = models.CharField(max_length=60)
    student_fname = models.CharField(max_length=40)
    student_lname = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'student'
