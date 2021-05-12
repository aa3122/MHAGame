<<<<<<< HEAD
from django.db import models

# Create your models here.
class Student(models.Model):
    stud_email = models.CharField(primary_key=True, max_length=60)
    password = models.CharField(max_length=60)
    student_fname = models.CharField(max_length=40)
    student_lname = models.CharField(max_length=40)

    def __str__(self):
        return '%s %s %s %s' % (self.stud_email, self.password, self.student_fname, self.student_lname)


    class Meta:
        managed = False
        db_table = 'student'
=======
from django.db import models

# Create your models here.
class Student(models.Model):
    stud_email = models.CharField(primary_key=True, max_length=60)
    password = models.CharField(max_length=60)
    student_fname = models.CharField(max_length=40)
    student_lname = models.CharField(max_length=40)

    def __str__(self):
        return '%s %s %s %s' % (self.stud_email, self.password, self.student_fname, self.student_lname)


    class Meta:
        managed = False
        db_table = 'student'
>>>>>>> 5f2acfd9036e68a7056ed2a43dcec6dae7927395
