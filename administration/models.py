from django.db import models

# Create your models here.
class Instructor(models.Model):
    inst_email = models.CharField(primary_key=True, max_length=60)
<<<<<<< HEAD
    #org = models.ForeignKey('Organization', models.DO_NOTHING, db_column='org_ID')  # Field name made lowercase.
=======
   # org = models.ForeignKey('Organization', models.DO_NOTHING, db_column='org_ID')  # Field name made lowercase.
>>>>>>> 1360cf667157ff4ed5f76ab389bf7044c6fcb126
    instructor_fname = models.CharField(max_length=40)
    instructor_lname = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'instructor'
