from django.db import models

# Create your models here.
class Instructor(models.Model):
    inst_email = models.CharField(primary_key=True, max_length=60)
    #org = models.ForeignKey('Organization', models.DO_NOTHING, db_column='org_ID')  # Field name made lowercase.
    instructor_fname = models.CharField(max_length=40)
    instructor_lname = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'instructor'