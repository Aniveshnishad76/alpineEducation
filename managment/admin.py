from django.contrib import admin

# Register your models here.
from managment.models import Student_Register, Student_Semester_Register, Faculty, MST_Result, Student_all, Otp, \
    Attendance, txn_details
from managment.models import Contact_Us

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('enrollment_number','course','semester','attendance')
    search_fields = ('enrollment_number','course','semester')
    list_per_page = 10
    list_filter = ('enrollment_number',)
    ordering = ('enrollment_number',)

class Contact_UsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'title','message')
    search_fields = ('first_name', 'last_name', 'email', 'title','message')
    list_per_page = 10

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'faculty_name', 'faculty_number', 'faculty_type', 'faculty_email','photo')
    seaech_fields = ('faculty_id', 'faculty_name', 'faculty_number', 'faculty_type', 'faculty_email')
    list_per_page = 10
    list_editable = ( 'faculty_name', 'faculty_number', 'faculty_type', 'faculty_email')
    ordering = ('faculty_name',)


class MST_ResultAdmin(admin.ModelAdmin):
    list_display = ('enrollment_number', 'faculty_id','mst', 'month', 'semester', 'subject')
    search_fields = ('enrollment_number', 'faculty_id','mst', 'month', 'semester', 'subject')
    list_per_page = 10
    ordering = ('enrollment_number',)

class Student_registerAdmin(admin.ModelAdmin):
    list_display = ('enrollment_number','name','contact_number','email')
    search_fields =  ('enrollment_number','name','contact_number','email')
    list_per_page = 10
    list_filter = ('enrollment_number',)
    ordering = ('enrollment_number',)

class Student_Semester_registerAdmin(admin.ModelAdmin):
    list_display = ('enrollment_number','name','status','contact_number','email','father_name','semester','course','address','photo','signature')
    search_fields = ('enrollment_number','name','status','contact_number','email','father_name','semester','course','address')
    list_per_page = 10
    list_filter = ('course',)
    ordering = ('enrollment_number',)

class Student_allAdmin(admin.ModelAdmin):
    list_display = ('enrollment_number', 'name','branch','semester_fees','previous_pending','total_pending')
    search_fields = ('enrollment_number', 'name','branch','semester_fees','previous_pending','total_pending')
    list_per_page = 10
    list_editable = ('semester_fees','previous_pending','total_pending')
    list_filter = ('branch',)
    ordering = ('enrollment_number',)



admin.site.register(Student_Register,Student_registerAdmin)
admin.site.register(Student_Semester_Register,Student_Semester_registerAdmin)
admin.site.register(Faculty,FacultyAdmin)
admin.site.register(MST_Result,MST_ResultAdmin)
admin.site.register(Student_all,Student_allAdmin)
admin.site.register(Contact_Us,Contact_UsAdmin)
admin.site.register(Otp)
admin.site.register(txn_details)
admin.site.register(Attendance,AttendanceAdmin)






admin.site.site_title = 'Alpine Institute Of Technology (AIT)'
admin.site.site_url = 'http://AlpineInstituteOfTechnology(AIT).com/'
admin.site.index_title = 'Alpine Institute Of Technology Admin Panel'
admin.empty_value_display = '**Empty**'
admin.site.site_header="Alpine Institute Of Technology (AIT) "