from django.db import models

# Create your models here.
from django.db.models import Model


class txn_details(Model):
    txnid=models.CharField(max_length=100,null=True)
    txndate=models.CharField(max_length=100,null=True)
    order_id=models.CharField(max_length=100,null=True)
    enrollment_number=models.CharField(max_length=200)
    amount=models.CharField(max_length=200,null=True)
    status=models.CharField(max_length=200,default='pending')

class Student_Register(Model):
    name=models.CharField(max_length=20)
    contact_number=models.CharField(max_length=10)
    email=models.EmailField(max_length=30)
    enrollment_number=models.CharField(max_length=12)
    password=models.CharField(max_length=16)

    def __str__(self):
        return self.enrollment_number
class Student_Semester_Register(Model):
    name=models.CharField(max_length=20)
    contact_number=models.CharField(max_length=10)
    enrollment_number=models.CharField(max_length=12)
    father_name=models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    semester = models.CharField(max_length=50)
    course = models.CharField(max_length=300)
    address = models.CharField(max_length=200)
    status=models.CharField(default='active',max_length=200)
    photo=models.ImageField(upload_to='media/Student_registration_photo/',default='media/person1.jpg')
    signature = models.ImageField(upload_to='media/Student_registration_signature/')
    def __str__(self):
        return self.enrollment_number


class Faculty(Model):
    faculty_id=models.CharField(max_length=50)
    faculty_name=models.CharField(max_length=30)
    faculty_password = models.CharField(max_length=30)
    DEPARTMENT_CHOOSE = (('Mechanical_Engineering_(BE)', 'Mechanical_Engineering_(BE)'),
                         ('Civil_Engineering_(BE)', 'Civil_Engineering_(BE)'),
                         ('Computer_Science_Engineering_(BE)', 'Computer_Science_Engineering_(BE)'),
                         ('Computer_Science_Engineering_(BE)', 'Computer_Science_Engineering_(BE)'),
                         ('Electrical_Engineering_(BE)', 'Electrical_Engineering_(BE)'),
                         ('Electronics_&_Comunication_Engineering_(BE)', 'Electronics_&_Comunication_Engineering_(BE)'),
                         ('Mechanical_Engineering_(B Tech)', 'Mechanical_Engineering_(B Tech)'),
                         ('Civil_Engineering_(B Tech)', 'Civil_Engineering_(B Tech)'),
                         ('Computer_Science_Engineering_(B Tech)', 'Computer_Science_Engineering_(B Tech)'),
                         ('Electrical_Engineering_(B Tech)', 'Electrical_Engineering_(B Tech)'), (
                         'Electronics_&_Comunication_Engineering_(B Tech)',
                         'Electronics_&_Comunication_Engineering_(B Tech)'), ('Mechanical_Engineering_(M Tech)', ''),
                         ('Civil_Engineering_(M Tech)', 'Civil_Engineering_(M Tech)'),
                         ('Computer_Science_Engineering_(M Tech)', 'Computer_Science_Engineering_(M Tech)'),
                         ('Electrical_Engineering_(M Tech)', 'Electrical_Engineering_(M Tech)'),
                         ('Electronics_&_Comunication_Engineering_(M Tech)',
                          'Electronics_&_Comunication_Engineering_(M Tech)'),
                         ('Human_Resources_Mangement_(MBA)', 'Human_Resources_Mangement_(MBA)'),
                         ('Financial_Management_(MBA)', 'Financial_Management_(MBA)'),
                         ('Systems_Management_(MBA)', 'Systems_Management_(MBA)'),
                         ('Mechanical_Engineering_(Diploma)', 'Mechanical_Engineering_(Diploma)'),
                         ('Electrical_Engineering_(Diploma)', 'Electrical_Engineering_(Diploma)'),
                         ('Electronics_and_Communication (Diploma)', 'Electronics_and_Communication (Diploma)'),
                         ('Civil_Engineering_(Diploma)', 'Civil_Engineering_(Diploma)'),
                         ('Computer_Science_and_Engineering_(Diploma)', 'Computer_Science_and_Engineering_(Diploma)'),
                         ('IT_Engineering_(Diploma)', 'IT_Engineering_(Diploma)'),
                         ('Chemical_Engineering_(Diploma)', 'Chemical_Engineering_(Diploma)'),
                         ('Mechanical_Engineering_(ITI)', 'Mechanical_Engineering_(ITI)'),
                         ('Tool_&_Die_Maker_Engineering_(ITI)', 'Tool_&_Die_Maker_Engineering_(ITI)'),
                         ('Pump_Operator_(ITI)', 'Pump_Operator_(ITI)'),
                         ('Civil_Engineering_(ITI )', 'Civil_Engineering_(ITI )'),
                         ('Fitter_Engineering_(ITI)', 'Fitter_Engineering_(ITI)'),
                         ('Computer_Engineering_(ITI)', 'Computer_Engineering_(ITI)'),
                         ('Turner_Engineering_(ITI)', 'Turner_Engineering_(ITI)'),
                         ('Bechelor_in_Pharmacy', 'Bechelor_in_Pharmacy'), ('Master_in_Pharmacy', 'Master_in_Pharmacy')
                         )


    department=models.CharField(max_length=300,choices=DEPARTMENT_CHOOSE)
    faculty_number=models.CharField(max_length=50)
    faculty_email = models.EmailField(max_length=50)
    TYPE=( ('Faculty','Faculty'),('HOD','HOD'))
    faculty_type=models.CharField(max_length=30, choices=TYPE ,blank=True)
    photo = models.ImageField(upload_to='media/faculty_photo/')
    def _str_(self):
        return self.faculty_id

class Student_all(Model):

        name = models.CharField(max_length=100)
        enrollment_number = models.CharField(max_length=100)
        DEPARTMENT_CHOOSE = (('Mechanical_Engineering_(BE)','Mechanical_Engineering_(BE)'),('Civil_Engineering_(BE)','Civil_Engineering_(BE)'),
        ('Computer_Science_Engineering_(BE)','Computer_Science_Engineering_(BE)'),('Computer_Science_Engineering_(BE)','Computer_Science_Engineering_(BE)'),
        ('Electrical_Engineering_(BE)','Electrical_Engineering_(BE)'),('Electronics_&_Comunication_Engineering_(BE)','Electronics_&_Comunication_Engineering_(BE)'),
        ('Mechanical_Engineering_(B Tech)','Mechanical_Engineering_(B Tech)'),('Civil_Engineering_(B Tech)','Civil_Engineering_(B Tech)'),('Computer_Science_Engineering_(B Tech)','Computer_Science_Engineering_(B Tech)'),
        ('Electrical_Engineering_(B Tech)','Electrical_Engineering_(B Tech)'),('Electronics_&_Comunication_Engineering_(B Tech)','Electronics_&_Comunication_Engineering_(B Tech)'),('Mechanical_Engineering_(M Tech)',''),
        ('Civil_Engineering_(M Tech)','Civil_Engineering_(M Tech)'),('Computer_Science_Engineering_(M Tech)','Computer_Science_Engineering_(M Tech)'),('Electrical_Engineering_(M Tech)','Electrical_Engineering_(M Tech)'),
        ('Electronics_&_Comunication_Engineering_(M Tech)','Electronics_&_Comunication_Engineering_(M Tech)'),('Human_Resources_Mangement_(MBA)','Human_Resources_Mangement_(MBA)'),('Financial_Management_(MBA)','Financial_Management_(MBA)'),('Systems_Management_(MBA)','Systems_Management_(MBA)'),('Mechanical_Engineering_(Diploma)','Mechanical_Engineering_(Diploma)'),('Electrical_Engineering_(Diploma)','Electrical_Engineering_(Diploma)'),('Electronics_and_Communication (Diploma)','Electronics_and_Communication (Diploma)'),('Civil_Engineering_(Diploma)','Civil_Engineering_(Diploma)'),('Computer_Science_and_Engineering_(Diploma)','Computer_Science_and_Engineering_(Diploma)'),('IT_Engineering_(Diploma)','IT_Engineering_(Diploma)'),('Chemical_Engineering_(Diploma)','Chemical_Engineering_(Diploma)'),
        ('Mechanical_Engineering_(ITI)','Mechanical_Engineering_(ITI)'),('Tool_&_Die_Maker_Engineering_(ITI)','Tool_&_Die_Maker_Engineering_(ITI)'),('Pump_Operator_(ITI)','Pump_Operator_(ITI)'),('Civil_Engineering_(ITI )','Civil_Engineering_(ITI )'),('Fitter_Engineering_(ITI)','Fitter_Engineering_(ITI)'),('Computer_Engineering_(ITI)','Computer_Engineering_(ITI)'),
                             ('Turner_Engineering_(ITI)','Turner_Engineering_(ITI)'),('Bechelor_in_Pharmacy','Bechelor_in_Pharmacy'),('Master_in_Pharmacy','Master_in_Pharmacy')
                             )
        branch = models.CharField(max_length=300,choices=DEPARTMENT_CHOOSE,blank=True)
        semester_fees = models.CharField(max_length=30, blank=True)
        previous_pending = models.CharField(max_length=30, blank=True)
        total_pending = models.CharField(max_length=30, blank=True)



        def _str_(self):
            return self.enrollment_number
class MST_Result(Model):
    enrollment_number=models.CharField(max_length=30)
    mst=models.CharField(max_length=30)
    month=models.CharField(max_length=30)
    semester=models.CharField(max_length=30)
    subject=models.CharField(max_length=130)
    marks_obtained=models.CharField(max_length=30)
    total_marks=models.CharField(max_length=30)
    faculty_id=models.CharField(max_length=50)
    def _str_(self):
        return self.enrollment_number

class Contact_Us(Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=60)
    title=models.CharField(max_length=50)
    message=models.CharField(max_length=300)
    def _str_(self):
        return self.email

class UserOTP(Model):
    enrollment_number=models.ForeignKey(Student_Register, on_delete=models.CASCADE)
    time_set=models.DateTimeField(auto_now= True)
    otp=models.CharField( max_length=5)

class Otp(Model):
    enrollment_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    otp= models.CharField(max_length=5)
    status = models.CharField(default="Vaild",max_length=20)
    def _str_(self):
        return self.enrollment_number
class Attendance(Model):
    enrollment_number= models.CharField(max_length=30)
    semester= models.CharField(max_length=30)
    course= models.CharField(max_length=30)
    attendance= models.CharField(max_length=30)
    date=models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return self.enrollment_number


