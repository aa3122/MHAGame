from django.contrib import admin
from login.models import Student, Organization, Instructor

class studentAdmin(admin.ModelAdmin):
	list_display=('stud_email','password','student_fname','student_lname')


class organizationAdmin(admin.ModelAdmin):
	list_display=('org_id', 'org_name')

class instructorAdmin(admin.ModelAdmin):
	list_display=('inst_email','org','instructor_fname','instructor_lname')

admin.site.register(Student, studentAdmin)
admin.site.register(Organization, organizationAdmin)
admin.site.register(Instructor,instructorAdmin)