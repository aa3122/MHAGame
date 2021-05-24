from django.db import models
from django.contrib.auth.models import User


class CourseSection(models.Model):
    crn = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    term = models.CharField(max_length=100)
    prefix = models.CharField(max_length=40)
    course_num = models.CharField(max_length=40)
    section_num = models.CharField(max_length=40)
    instructor = models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name = 'instructor',limit_choices_to={'is_staff': True},)

    class Meta:
        managed = True
        db_table = 'course_section'
    def __str__(self):
        return (self.prefix + ' ' + self.course_num + '-' + self.section_num +  ' Instructor: ' + str(self.instructor))

class Class(models.Model):
    classid = models.AutoField(primary_key=True)
    course = models.ForeignKey(CourseSection,on_delete=models.CASCADE)
    student = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'student', limit_choices_to={'is_staff': False},)

    class Meta:
        managed = True
        db_table = 'class'

    def __str__(self):
        return (str(self.course) + '| Student: ' + str(self.student))


    