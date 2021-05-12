from django.db import models

# Create your models here.
class Student(models.Model):
    stud_email = models.CharField(primary_key=True, max_length=60)
    password = models.CharField(max_length=60)
    student_fname = models.CharField(max_length=40)
    student_lname = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'student'

	
