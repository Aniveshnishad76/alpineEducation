from paytm import Checksum

import datetime
import random

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import get_template
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt

from managment.models import Student_Register, Student_Semester_Register, Faculty, Student_all, MST_Result, Contact_Us, \
    Otp, Attendance, txn_details



def Index_page(request):
    return render(request,"index.html")
def Home_page(request):

    return render(request,"index.html")
def Courses_page(request):
    return render(request,"courses.html")
def Faculty_page(request):
    x=Faculty.objects.all()
    return render(request,"faculty.html",{"data":x})
def About_page(request):
    return render(request,"about.html")
def Contact_page(request):
    return render(request,"contact.html")
def Student_login(request):
    return render(request, "student_pages/student_login.html")
def Student_register(request):
    return render(request, "student_pages/student_register.html")





def Data_register(request):
    msg=""
    if request.method=="POST":
        name=request.POST['name']
        contact_number = request.POST['contact_number']
        email = request.POST['email']
        enrollment_number = request.POST['enrollment_number']
        password = request.POST['password']

        if Student_all.objects.filter(enrollment_number=enrollment_number).exists():
            if Student_Register.objects.filter(enrollment_number=enrollment_number).exists():
                messages.error(request,"Enrollment Number is Already Registered")
                return render(request, "student_pages/student_register.html")
            elif Student_Register.objects.filter(contact_number=contact_number).exists():
                messages.error(request, "Mobile Number is Already Registered")
                return render(request, "student_pages/student_register.html")
            elif Student_Register.objects.filter(email=email).exists():
                messages.error(request, "Email is Already Registered")
                return render(request, "student_pages/student_register.html")
            else:
                user=Student_Register(name=name,contact_number=contact_number,email=email,enrollment_number=enrollment_number,password=password,)
                ctx={
                    'content': 'message'
                    }
                message=get_template('student_pages/email_tamplate1.html').render(ctx)
                msg=EmailMessage(
                    'AIT Registration',
                    message,
                    'Alpine Insitude Of Techonology',
                    [email],

                )
                msg.content_subtype="html"
                msg.send()
                user.save()
                messages.success(request,"You are register successfuly Please Login")
                return render(request,"student_pages/student_login.html")
        else:
            messages.error(request,"Your are not a student of AIT")
            return render(request,"student_pages/student_register.html",)
    else:
        msg="REGISTERED FAILED"
    return render(request,"student_pages/student_register.html")
def Data_login(request):

    if request.method =="POST":
        enrollment_number=request.POST['enrollment_number']
        password=request.POST['password']
        if Student_Register.objects.filter(enrollment_number=enrollment_number,password=password).exists():
            request.session['enrollment_number']=enrollment_number
            x=Student_Register.objects.get(enrollment_number=enrollment_number)
            name=x.name
            messages.success(request,"Login Successfuly")
            return render(request,"student_pages/student_home.html",{"enrollment_number":enrollment_number,'data':x,"name":name})
        else:
            messages.error(request,"Invalid Enrollment or Password ")
            return render(request,"student_pages/student_login.html")
    return render(request, "student_pages/student_login.html")

def Student_home(request):
    try:
        if request.session['enrollment_number'] is not None:
            enrollment_number=request.session['enrollment_number']
            obj=Student_Register.objects.get(enrollment_number=enrollment_number)
            name=obj.name
            if Student_Semester_Register.objects.filter(enrollment_number=enrollment_number,status="active"):
                x = Student_Semester_Register.objects.get(enrollment_number=enrollment_number,status="active")
                return render(request,"student_pages/student_home.html",{"name":name,"photo":x})
            else:
                photo="media/media/person1.jpg"
                return render(request, "student_pages/student_home.html", {"name": name,"pic":photo})
        else:
            return render(request, "student_pages/student_login.html")
    except:
         return render(request, "student_pages/student_login.html")
            


def Student_registration(request):
    try:
        if request.session['enrollment_number'] is not None:
            enrollment_number = request.session['enrollment_number']
            x = Student_Register.objects.get(enrollment_number=enrollment_number)
            return render(request,"student_pages/student_registration.html",{"enrollment_number":enrollment_number,"data":x})
        else:
            return render(request, "student_pages/student_login.html")
    except:
         return render(request, "student_pages/student_login.html")
            
def Student_profile(request):
    try:
        if request.session['enrollment_number'] is not None:
            enrollment_number=request.session['enrollment_number']
            if Student_Semester_Register.objects.filter(enrollment_number=enrollment_number,status='active'):
                x=Student_Semester_Register.objects.get(enrollment_number=enrollment_number, status='active')
                return render(request,"student_pages/student_profile.html",{"data":x,"enrollment_number":enrollment_number})
            else:
                messages.error(request,"Please Complete Your Profile")
                return redirect( Student_registration)
        else:
            return render(request, "student_pages/student_login.html")
    except:
         return render(request, "student_pages/student_login.html")


def Update_student_profile(request,id):
    try:
        if request.session['enrollment_number'] is not None:
            if request.method=="POST":
                up=Student_Semester_Register.objects.get(id=id)
                up.name=request.POST['name']
                up.contact_number = request.POST['contact_number']
                up.address=request.POST['address']
                up.save()
                messages.success(request,'Saved Successfuly')
                return render(request,"student_pages/student_home.html")
            else:
                messages.error(request,'Profile Not Saved')
                return render(request,"student_pages/student_profile.html")
        else:
            return render(request, "student_pages/student_login.html")
    except:
         return render(request, "student_pages/student_login.html")

def Student_mstresult(request):
    try:
        if request.session['enrollment_number'] is not None:
            enrollment_number=request.session['enrollment_number']
            x=MST_Result.objects.filter(enrollment_number=enrollment_number)
            return render(request,"student_pages/student_mstresult.html",{"x":x})
        else:
            return render(request, "student_pages/student_login.html")
    except:
         return render(request, "student_pages/student_login.html")
def Student_registration_form(request):
    try:
        if request.session['enrollment_number'] is not None:
            if request.method=="POST":
                name=request.POST['name']
                contact_number = request.POST['contact_number']
                enrollment_number = request.session['enrollment_number']
                father_name = request.POST['father_name']
                email = request.POST['email']
                semester= request.POST['semester']
                course= request.POST['course']
                address = request.POST['address']
                photo = request.FILES['photo']
                signature = request.FILES['signature']
                if Student_Semester_Register.objects.filter(Q(enrollment_number=enrollment_number,status='active')|Q(enrollment_number=enrollment_number,semester=semester)).exists():

                    messages.error(request,"Enrollment number Is already registered")

                    return redirect( Student_registration)
                else:
                    user = Student_Semester_Register(name=name, contact_number=contact_number,enrollment_number=enrollment_number, father_name=father_name,email=email, semester=semester, course=course, address=address,photo=photo, signature=signature)
                    ctx = {
                        'name': name,
                        'sem':semester,
                        'course':course,
                        'enroll':enrollment_number,
                        'photo':photo
                    }
                    message = get_template('student_pages/email_tamplate2.html').render(ctx)
                    msg = EmailMessage(
                        'AIT Registration',
                        message,
                        'Alpine Insitude Of Techonology',
                        [email],

                    )
                    msg.content_subtype = "html"
                    msg.send()
                    user.save()

                    request.session['enrollment_number'] = enrollment_number
                    enrollment_number = request.session['enrollment_number']
                    if semester > '1':
                        f = Student_all.objects.get(enrollment_number=enrollment_number)
                        f.previous_pending = f.total_pending
                        f.total_pending = float(f.total_pending) + float(f.semester_fees)
                        f.save()
                        x = Student_Register.objects.get(enrollment_number=enrollment_number)
                        messages.success(request, "YOUR REGISTERATION IS SUCCESSFULL!")
                        return render(request, "student_pages/student_home.html", { "data": x})
                    else:
                        x = Student_Register.objects.get(enrollment_number=enrollment_number)
                        messages.success(request, "YOUR REGISTERATION IS  SUCCESSFULL!")
                        return render(request, "student_pages/student_home.html", { "data": x})

            else:
                messages.error(request,"REGISTERATION FAILED")
            return render(request,"student_pages/student_registration.html")
        else:
            return render(request, "student_pages/student_login.html")
    except:
         return render(request, "student_pages/student_login.html")
        

def Your_registration(request):
    try:
        if request.session['enrollment_number'] is not None:
   
            enrollment_number=request.session['enrollment_number']

            if Student_Semester_Register.objects.filter(enrollment_number=enrollment_number,status='active'):
                x = Student_Semester_Register.objects.get(enrollment_number=enrollment_number, status='active')
                return render(request, "student_pages/Your_registration.html", { "enrollment_number": enrollment_number,"data":x})
            else:
                messages.error(request,'You are Not Registered Yet For Semester ! Please Register Your Semester')
                return redirect( Student_registration)
        else:
           return render(request, "student_pages/student_login.html")
    except:
         return render(request, "student_pages/student_login.html")
    
def Update_registration_form(request,id):
    
    try:
        if request.session['enrollment_number'] is not None:

            if request.method == "POST":
                up = Student_Semester_Register.objects.get(id=id)
                up.name = request.POST['name']
                up.father_name = request.POST['father_name']
                up.semester = request.POST['semester']
                up.course = request.POST['course']
                up.address = request.POST['address']
                up.photo = request.FILES['photo']
                up.signature = request.FILES['signature']
                up.save()
                messages.success(request, "Saved Successfully")
                return render(request,"student_pages/student_home.html")
            else:
                messages.error(request,"registration form not save")
                return render(request, "student_pages/student_registration.html")
        else:
            return render(request, "student_pages/student_login.html")
    except:
         return render(request, "student_pages/student_login.html")

def Faculty_login(request):
    return render(request,"faculty_pages/faculty_login.html")

def Faculty_data_login(request):
    msg = ""
    if request.method == "POST":
        faculty_number= request.POST['faculty_number']
        faculty_password = request.POST['faculty_password']
        if Faculty.objects.filter(faculty_number=faculty_number,faculty_password=faculty_password).exists():
            request.session['faculty_number'] =faculty_number
            x = Faculty.objects.get(faculty_number=faculty_number)
            messages.success(request,'Login Successfuly')
            return render(request, "faculty_pages/faculty_home.html",{"faculty_number": faculty_number, 'data': x})
        else:
            messages.error(request, "INVALID USERID OR PASSWORD")
            return render(request, "faculty_pages/faculty_login.html")
    return render(request, "faculty_pages/faculty_login.html")

def Faculty_home(request):
    try:
        if request.session['faculty_number'] is not None:
            return render(request,"faculty_pages/faculty_home.html")
        else:
            return render(request, "faculty_pages/faculty_login.html")
    except:
         return render(request, "faculty_pages/faculty_login.html")
def Faculty_profile(request):
    try:
        if request.session['faculty_number'] is not None:
            faculty_number = request.session['faculty_number']
            x = Faculty.objects.get(faculty_number=faculty_number)
            return render(request, "faculty_pages/faculty_profile.html", {"data": x, "faculty_number": faculty_number})
        else:
            return render(request, "faculty_pages/faculty_login.html")
    except:
         return render(request, "faculty_pages/faculty_login.html")
def Update_faculty_profile(request,id):
    try:
        if request.session['faculty_number'] is not None:
            if request.method=="POST":
                up=Faculty.objects.get(id=id)
                up.faculty_name=request.POST['faculty_name']
                up.faculty_number = request.POST['faculty_number']
                up.faculty_email=request.POST['faculty_email']
                up.photo=request.FILES['photo']
                up.save()
                messages.success(request,"Saved Successfully")
                return render(request,"faculty_pages/faculty_home.html")
            else:
                messages.error(request,"Profile not save")
                return render(request,"faculty_pages/faculty_profile.html")
        else:
            return render(request, "faculty_pages/faculty_login.html")
    except:
         return render(request, "faculty_pages/faculty_login.html")

def Show_student_registration_form(request):
    try:
        if request.session['faculty_number'] is not None:
            return render(request,"faculty_pages/show_student_registration_form.html")
        else:
            return render(request, "faculty_pages/faculty_login.html")
    except:
         return render(request, "faculty_pages/faculty_login.html")
def Show_student_registration_formm(request):
    try:
        if request.session['faculty_number'] is not None:
            if request.method == "POST":
                semester=request.POST['semester']
                course=request.POST['course']
                y=Student_Semester_Register.objects.filter(semester=semester,course=course,status="active")
                return render(request,"faculty_pages/show_student_registration_form.html",{"data":y})
        else:
            return render(request, "faculty_pages/faculty_login.html")
    except:
         return render(request, "faculty_pages/faculty_login.html")

def logout(request):
    try:
        request.session.flush()
    except:
        pass
    messages.success(request,'Logout Successfuly')
    return redirect("Data_login")
def Faculty_logout(request):
    try:
        request.session.flush()
    except:
        pass
    messages.success(request,'Logout successfuly')
    return redirect("Faculty_data_login")
def view_mst_details(request,mst):
    try:
        if request.session['enrollment_number'] is not None:
            enrollment_number=request.session['enrollment_number']
            x=MST_Result.objects.filter(enrollment_number=enrollment_number,mst=mst)
            return render(request,"student_pages/view_mst_details.html",{"x":x})
        else:
            return render(request, "student_pages/student_login.html")
    except:
         return render(request, "student_pages/student_login.html")

def Add_student(request):
    try:
        if request.session['faculty_number'] is not None:
            return render(request,"faculty_pages/add_student.html")
        else:
            return render(request, "faculty_pages/faculty_login.html")
    except:
         return render(request, "faculty_pages/faculty_login.html")
def Add_MST_Marks(request):
    try:
        if request.session['faculty_number'] is not None:
            return render(request,"faculty_pages/add_mst_marks.html")
        else:
            return render(request, "faculty_pages/faculty_login.html")
    except:
         return render(request, "faculty_pages/faculty_login.html")
def Check_no_Dues(request):
    try:
        if request.session['faculty_number'] is not None:
            if request.method=="POST":
                course=request.POST['course']
                semester = request.POST['semester']
                check = request.POST['check']
                if check=="1":
                    if Student_Semester_Register.objects.filter(course=course,semester=semester,status="active"):
                        obj=Student_all.objects.filter(branch=course,previous_pending__gte=1)

                        return render(request,"faculty_pages/check_no_dues.html",{"obj":obj})
                else:
                    if Student_Semester_Register.objects.filter(course=course, semester=semester, status="active"):
                        obj = Student_all.objects.filter(branch=course, previous_pending=0)
                        return render(request, "faculty_pages/check_no_dues.html", {"obj": obj})

            return render(request,"faculty_pages/check_no_dues.html")
        else:
            return render(request, "faculty_pages/faculty_login.html")
    except:
         return render(request, "faculty_pages/faculty_login.html")
def do_add_student(request):
    try:
        if request.session['faculty_number'] is not None:

            if request.method=="POST":

                faculty_number = request.session['faculty_number']

                name=request.POST['name']
                enrollment_number=request.POST['enrollment_number']
                branch=request.POST['branch']
                if Student_all.objects.filter(enrollment_number=enrollment_number):
                    messages.error(request,"Student Already Added")
                    return render(request, 'faculty_pages/add_student.html')
                elif Faculty.objects.filter(faculty_number=faculty_number,faculty_type='HOD'):
                        obj=Student_all(name=name,enrollment_number=enrollment_number,branch=branch)
                        obj.save()
                        messages.success(request,'Student Add Succesfully')
                        return render(request,'faculty_pages/add_student.html')
                else:
                    messages.error(request,"Student Can Add Only By HOD ")
                    return render(request, 'faculty_pages/add_student.html')

            else:
                messages.error(request,'Student Not Add Sucessfuly')
                return render(request, 'faculty_pages/add_student.html')
        else:
            return render(request, "faculty_pages/faculty_login.html")
    except:
         return render(request, "faculty_pages/faculty_login.html")
def do_add_mst_marks(request):
    try:
        if request.session['faculty_number'] is not None:
            if request.method=="POST":
                faculty_id=request.session['faculty_number']
                enrollment_number=request.POST['enrollment_number']
                mst=request.POST['mst']
                month=request.POST['month']
                semester= request.POST['semester']
                subject = request.POST['subject']
                marks_obtained = request.POST['marks_obtained']
                total_marks = request.POST['total_marks']
                if MST_Result.objects.filter(enrollment_number=enrollment_number,semester=semester,subject=subject,mst=mst):
                    messages.error(request,"Marks Already Added")
                    return render(request,'faculty_pages/add_mst_marks.html')
                else:
                    obj=MST_Result(enrollment_number=enrollment_number,mst=mst,month=month,semester=semester,subject=subject,marks_obtained=marks_obtained,total_marks=total_marks,faculty_id=faculty_id)
                    obj.save()
                    messages.success(request,'Maeks Added Successfuly')
                    return render(request, 'faculty_pages/add_mst_marks.html')
            else:
                messages.error(request,'Marks Not Added')
                return render(request, 'faculty_pages/add_mst_marks.html')
        else:
            return render(request, "faculty_pages/faculty_login.html")
    except:
         return render(request, "faculty_pages/faculty_login.html")
def View_MST_Marks(request):
    try:
        if request.session['faculty_number'] is not None:
            faculty_id=request.session['faculty_number']
            obj=MST_Result.objects.filter(faculty_id=faculty_id)
            return render(request,'faculty_pages/View_MST_Marks.html',{"data":obj})
        else:
            return render(request, "faculty_pages/faculty_login.html")
    except:
         return render(request, "faculty_pages/faculty_login.html")
def View_MST_Markss(request):
    try:
        if request.session['faculty_number'] is not None:
            faculty_id=request.session['faculty_number']
            enrollment_number = request.POST['enrollment_number']
            obj=MST_Result.objects.filter(faculty_id=faculty_id,enrollment_number=enrollment_number)
            return render(request,'faculty_pages/View_MST_Marks.html',{"data":obj})
        else:
            return render(request, "faculty_pages/faculty_login.html")
    except:
         return render(request, "faculty_pages/faculty_login.html")

def delete_student(request):
    try:
        if request.session['faculty_number'] is not None:
            if request.method == "POST":
                id = request.POST.get('id')
                

                obj = MST_Result.objects.get(id=id)
                obj.delete()
                return JsonResponse({'status': 'delete'})
            else:
                return JsonResponse({"status": 'error'})
        else:
            return render(request, "faculty_pages/faculty_login.html")
    except:
         return render(request, "faculty_pages/faculty_login.html")


def update_student(request,id):
    try:
        if request.session['faculty_number'] is not None:
            obj=MST_Result.objects.get(id=id)
            return render(request,'faculty_pages/update_student_mst_marks.html',{"data":obj})
        else:
            return render(request, "faculty_pages/faculty_login.html")
    except:
         return render(request, "faculty_pages/faculty_login.html")
def do_update_mst_marks(request,id):
    try:
        if request.session['faculty_number'] is not None:
            if request.method=="POST":
                y=MST_Result.objects.get(id=id)
                y.faculty_id = request.session['faculty_number']
                y.enrollment_number = request.POST['enrollment_number']
                y.mst = request.POST['mst']
                y.month = request.POST['month']
                y.semester = request.POST['semester']
                y.subject = request.POST['subject']
                y.marks_obtained = request.POST['marks_obtained']
                y.total_marks = request.POST['total_marks']
                y.save()
                messages.success(request,"Update Successfulluy")
                return redirect(View_MST_Marks)
            else:
                messages.error(request,'Not Updated')
                return render(request, 'faculty_pages/View_MST_Marks.html')
        else:
            return render(request, "faculty_pages/faculty_login.html")
    except:
         return render(request, "faculty_pages/faculty_login.html")
def View_add_student(request):
    try:
        if request.session['faculty_number'] is not None:
            obj = Student_all.objects.all()
            return render(request,'faculty_pages/View_add_student.html',{'data':obj})
        else:
            return render(request, "faculty_pages/faculty_login.html")
    except:
         return render(request, "faculty_pages/faculty_login.html")


def View_add_studentt(request):
    try:
        if request.session['faculty_number'] is not None:
            if request.method=="POST":
                branch=request.POST['branch']
                obj=Student_all.objects.filter(branch=branch)
                return render(request, 'faculty_pages/View_add_student.html',{'data':obj})
        else:
            return render(request, "faculty_pages/faculty_login.html")
    except:
         return render(request, "faculty_pages/faculty_login.html")

def delete_added_student(request):
    try:
        if request.session['faculty_number'] is not None:
            if request.method=="POST":
                id=request.POST.get('id')
               

                obj=Student_all.objects.get(id=id)
                obj.delete()
                return JsonResponse({'status':'delete'})
            else:
                return JsonResponse({"status":'error'})
        else:
            return render(request, "faculty_pages/faculty_login.html")
    except:
         return render(request, "faculty_pages/faculty_login.html")
def update_added_student(request,id):
    try:
        if request.session['faculty_number'] is not None:
            obj=Student_all.objects.get(id=id)
            return render(request,'faculty_pages/update_added_student.html',{"data":obj})
        else:
            return render(request, "faculty_pages/faculty_login.html")
    except:
         return render(request, "faculty_pages/faculty_login.html")
def do_update_added_student(request,id):
    try:
        if request.session['faculty_number'] is not None:
            if request.method=="POST":
                y=Student_all.objects.get(id=id)
                y.faculty_id = request.session['faculty_number']
                y.name= request.POST['name']
                y.enrollment_number= request.POST['enrollment_number']
                y.branch= request.POST['branch']
                y.save()
                messages.success(request,"Update Successfulluy")
                return redirect(View_add_student)
            else:
                messages.error(request,"Not Updated")
                return render(request, 'faculty_pages/View_add_student.html')
        else:
            return render(request, "faculty_pages/faculty_login.html")
    except:
         return render(request, "faculty_pages/faculty_login.html")

def Contact_View(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        title=request.POST['title']
        message=request.POST['message']
        user=Contact_Us( first_name=first_name,last_name=last_name,email=email,title=title,message=message,)
        user.save()
        messages.success(request,'Message send successfuly')
        return render(request,"index.html")
    else:
        messages.error(request,'Not Contact yet')
        return render(request,"index.html")
def forget_password(request):
    return render(request,'student_pages/forgetpassword.html')
def do_forget_password(request):
    if request.method=="POST":
        enrollment_number=request.POST['enrollment_number']
        if Student_Register.objects.filter(enrollment_number=enrollment_number):
            obj=Student_Register.objects.get(enrollment_number=enrollment_number)
            email=obj.email
            otp=random.randint(10000,99999)
            otpp=str(otp)
            y=Otp(enrollment_number=enrollment_number,email=email,otp=otp)
            request.session['enrollment_number']=enrollment_number
            send_mail(
                'AIT Forget Pasword',
                'your one time password for changing your password is '+otpp,
                'Alpine Insitude Of Techonology',
                [email],

            )
            y.save()
        else:
            messages.WARNING(request,"Chack Your Enrollment Number")
            return render(request,"student_pages/forgetpassword.html")
        return render(request, "student_pages/enterotp.html",{"email":email})

    else:
        messages.ERROR(request,"error Occured Please Try After Sometime")
        return render(request,'student_pages/forgetpassword.html')
def enter_otp(request):
    if request.method=="POST":
        enrollment_number=request.session['enrollment_number']
        otp=request.POST['otp']
        if Otp.objects.filter(enrollment_number=enrollment_number,otp=otp,status="Vaild"):
            o = Otp.objects.filter(enrollment_number=enrollment_number, status="Vaild")
            for c1 in o:
                p = Otp.objects.get(id=c1.id)
                p.status = "complete"
                p.save()
            return render(request,'student_pages/new_password.html',{"enrollment_number":enrollment_number})
        else:
            messages.ERROR(request,"Invalid OTP")
            return render(request,'student_pages/enterotp.html')
        messages.ERROR(request,"Invalid OTP")
        return render(request,'student_pages/enterotp.html')
def do_new_password(request):
    if request.method=="POST":
        enrollment_number=request.session['enrollment_number']
        obj=Student_Register.objects.get(enrollment_number=enrollment_number)
        obj.password=request.POST['password']
        obj.save()
        request.session.flush()
        messages.success(request,"Password Change successfully please login ")
        return render(request,"student_pages/student_login.html")
    else:
        messages.error(request,"Password NOt Change yet!")
        return render(request, "student_pages/student_login.html")

def complete_status(request):
    try:
        if request.session['faculty_number'] is not None:
            if request.method=="POST":
                faculty_number=request.session['faculty_number']
                obj=Faculty.objects.get(faculty_number=faculty_number)
                faculty_type=obj.faculty_type
                faculty_id=obj.faculty_id
                if faculty_type=="HOD":
                   branch=request.POST['course']
                   semester = request.POST['semester']
                   if ((branch=="Computer_Science_Engineering_(B Tech)" and faculty_id=="HOD_CS_001") or (branch=="Computer_Science_Engineering_(BE)" and faculty_id=="HOD_CS_001")or (branch=="Mechanical_Engineering_(BE)" and faculty_id=="HOD_ME_001") or (branch=="Civil_Engineering_(BE)" and faculty_id=="HOD_CE_001")or (branch=="Electrical_Engineering_(BE)" and faculty_id=="HOD_EE_001") or (branch=="Electronics_&_Comunication_Engineering_(BE)" and faculty_id=="HOD_ECE_001")or (branch=="Mechanical_Engineering_(B Tech)" and faculty_id=="HOD_ME_001") or (branch=="Civil_Engineering_(B Tech)" and faculty_id=="HOD_CE_001")or (branch=="Electrical_Engineering_(B Tech)" and faculty_id=="HOD_EE_001") or (branch=="Electronics_&_Comunication_Engineering_(B Tech)" and faculty_id=="HOD_ECE_001")or (branch=="Mechanical_Engineering_(M Tech)" and faculty_id=="HOD_ME_001") or (branch=="Civil_Engineering_(M Tech)" and faculty_id=="HOD_CE_001")or (branch=="Computer_Science_Engineering_(M Tech)" and faculty_id=="HOD_CS_001") or (branch=="Electrical_Engineering_(M Tech)" and faculty_id=="HOD_EE_001") or (branch=="Electronics_&_Comunication_Engineering_(M Tech)" and faculty_id=="HOD_ECE_001")or (branch=="Human_Resources_Mangement_(MBA)" and faculty_id=="HOD_MBA_HRM_001") or (branch=="Financial_Management_(MBA)" and    faculty_id=="HOD_MBA_FM_001")or (branch=="Systems_Management_(MBA)" and faculty_id=="HOD_MBA_SM_001") ):
                       if Student_Semester_Register.objects.filter(course=branch,semester=semester):
                           c=Student_Semester_Register.objects.filter(course=branch,semester=semester,status="active")
                           #dd
                           for c1 in c:
                               p=Student_Semester_Register.objects.get(id=c1.id)
                               p.status = "complete"
                               p.save()
                       messages.success(request,"Stauts Complete Successfully")
                       return render(request,"faculty_pages/show_student_registration_form.html")
                   else:
                       messages.error(request, "Check Your Branch ")
                       return render(request,"faculty_pages/show_student_registration_form.html")
                else:
                    messages.error(request, " You are Not HOD")
                    return render(request, "faculty_pages/show_student_registration_form.html")
            else:
                messages.error(request, "Something Error")
                return render(request, "faculty_pages/show_student_registration_form.html")
        else:
            return render(request, "faculty_pages/faculty_login.html")
    except:
         return render(request, "faculty_pages/faculty_login.html")


def No_dues(request):
    enrollment_number=request.session['enrollment_number']
    obj=Student_all.objects.get(enrollment_number=enrollment_number)
    return render(request,'student_pages/no_dues.html',{"data":obj})

def transactions(request):
    enrollment_number = request.session['enrollment_number']
    obj=txn_details.objects.filter(enrollment_number=enrollment_number)
    return render(request,'student_pages/transaction.html',{'data':obj})


def checkout(request):

    email = 'paragmodi26@gmail.com'
    amount = request.POST['fees']
    order_id=random.randint(10000,99999)
    enrollment_number=request.session['enrollment_number']
    if txn_details.objects.filter(enrollment_number=enrollment_number,order_id=order_id).exists():
        messages.error(request,'something error')
        return redirect(No_dues)
    else:
        obj=txn_details(enrollment_number=enrollment_number,order_id=order_id)
        obj.save()
        param_dict = {
            'MID': 'PNessc34961607291218',#merchant id
            'ORDER_ID': str(order_id), #orderid genrated in our backend
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email, #customer email
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',#webstaging is used if we are in test mode
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'https://ait1.herokuapp.com/handlerequest/',
        }
        MERCHANT_KEY='g1hh%AmB#KagHbO3'
        param_dict['CHECKSUMHASH']=Checksum.generate_checksum(param_dict, MERCHANT_KEY)

        return render(request,"student_pages/paytm.html",{'param_dict':param_dict})

@csrf_exempt
def handlerequest(request):
    form=request.POST
    response_dict={}
    for i in form.keys():
        response_dict[i]=form[i]
        if i =="CHECKSUMHASH":
            checksum=form[i]
    MERCHANT_KEY = 'g1hh%AmB#KagHbO3'
    verify=Checksum.verify_checksum(response_dict,MERCHANT_KEY,checksum)
    if verify:
        if response_dict['RESPCODE']=='01':
            print("sucees")
            amount=response_dict['TXNAMOUNT']
            order_id = response_dict['ORDERID']
            print(response_dict)
            print(order_id)
            data=txn_details.objects.get(order_id=order_id)
            data.txnid=response_dict['TXNID']
            data.txndate = response_dict['TXNDATE']
            data.amount = response_dict['TXNAMOUNT']
            data.status ='success'
            data.save()

            fees = float(amount)
            main=txn_details.objects.get(order_id=order_id)
            enrollment_number = main.enrollment_number
            obj = Student_all.objects.get(enrollment_number=enrollment_number)
            pp = float(obj.previous_pending)
            if pp == fees:
                obj.previous_pending = 0
                obj.total_pending = float(obj.total_pending) - fees
                obj.save()
                return redirect(No_dues)
            elif pp > fees:
                obj.previous_pending = float(obj.previous_pending) - fees
                obj.total_pending = float(obj.total_pending) - fees
                obj.save()
                return redirect(No_dues)
            else:
                obj.previous_pending = 0
                obj.total_pending = float(obj.total_pending) - fees
                obj.save()
                return redirect(No_dues)




        else:
            print("fail")
            amount = response_dict['TXNAMOUNT']
            order_id = response_dict['ORDERID']
            print(response_dict)
            print(order_id)
            data = txn_details.objects.get(order_id=order_id)
            data.txnid = response_dict['TXNID']
            data.txndate = response_dict['TXNDATE']
            data.amount = response_dict['TXNAMOUNT']
            data.status = 'failed'
            data.save()
            return render(request, "student_pages/success.html", {'response': response_dict})

    print(response_dict)

    return render(request,"student_pages/success.html",{'response':response_dict})


def payfees(request):
    try:
        if request.session['enrollment_number'] is not None:
            if request.method=="POST":
                fees=float(request.POST['fees'])
                enrollment_number=request.session['enrollment_number']
                obj=Student_all.objects.get(enrollment_number=enrollment_number)
                pp=float(obj.previous_pending)
                if pp==fees:
                    obj.previous_pending=0
                    obj.total_pending=float(obj.total_pending)-fees
                    obj.save()

                    return redirect(No_dues)
                elif pp>fees:
                    obj.previous_pending = float(obj.previous_pending)-fees
                    obj.total_pending = float(obj.total_pending) - fees
                    obj.save()
                    return redirect(No_dues)
                else:
                    obj.previous_pending = 0
                    obj.total_pending = float(obj.total_pending) - fees
                    obj.save()
                    return redirect(No_dues)
                
                return render(request,'student_pages/no_dues.html')
            else:
                return render(request,'student_pages/no_dues.html')
        else:
            return render(request,"student_pages/student_login.html")
    except:
        return render(request,"student_pages/student_login.html")
     
def Student_attendence(request):
    try:
        if request.session['faculty_number'] is not None:
            return render(request, "faculty_pages/Student_attendence.html")
        else:
            return render(request, "faculty_pages/faculty_login.html")
    except:
        return render(request, "faculty_pages/faculty_login.html")
    
        
def do_Student_attendence(request):
    if request.method=="POST":
        course=request.POST['course']
        semester=request.POST['semester']
        p=Student_Semester_Register.objects.filter(course=course,semester=semester,status="active")
        return render(request, "faculty_pages/Student_attendence.html",{"data":p})
    else:
        return render(request,"faculty_pages/Student_attendence.html")
def absent(request):
    if request.method == "POST":
        enrollment_number=request.POST.get('enrollment_number')
        print(enrollment_number)
        o = Student_Semester_Register.objects.get(enrollment_number=enrollment_number, status="active")
        course = o.course
        semester = o.semester

        p = Attendance(enrollment_number=enrollment_number, course=course, semester=semester, attendance="absent")
        p.save()
        return JsonResponse({'status':'Absent'})
    else:
        return JsonResponse({'status':'error'})

    return redirect(do_Student_attendence)


def present(request):
    if request.method == "POST":
        enrollment_number = request.POST.get('enrollment_number')
        print(enrollment_number)
        o = Student_Semester_Register.objects.get(enrollment_number=enrollment_number, status="active")
        course = o.course
        semester = o.semester

        p = Attendance(enrollment_number=enrollment_number, course=course, semester=semester, attendance="present")
        p.save()
        return JsonResponse({'status': 'Present'})
    else:
        return JsonResponse({'status': 'error'})

    return redirect(do_Student_attendence)
def Resend_otp(request,email):
    enrollment_number=request.session['enrollment_number']
    if Student_Register.objects.filter(email=email,enrollment_number=enrollment_number):
        obj = Student_Register.objects.get(email=email)
        email = obj.email
        otp = random.randint(10000, 99999)
        otpp = str(otp)
        y = Otp(enrollment_number=enrollment_number, email=email, otp=otp)
        request.session['enrollment_number'] = enrollment_number
        send_mail(
            'AIT Forget Pasword',
            'your one time password for changing your password is ' + otpp,
            'Alpine Insitude Of Techonology',
            [email],

        )
        y.save()
    else:
        messages.WARNING(request, "Chack Your Enrollment Number")
        return render(request, "student_pages/forgetpassword.html")
    return render(request, "student_pages/enterotp.html", {"email": email})

def Your_attendence(request):
    try:
        if request.session['enrollment_number'] is not None:
            enrollment_number=request.session['enrollment_number']
            x=Attendance.objects.filter(enrollment_number=enrollment_number).order_by('-id')
            return render(request,"student_pages/your_attendence.html",{"data":x})
        else:
            return render(request, "student_pages/student_login.html")
    except:
         return render(request, "student_pages/student_login.html")

def Send_pending_email(request):
    if request.method=="POST":
        course=request.POST['course']
        semester=request.POST['semester']
        check=request.POST['check']
        if check=="1":
            if Student_Semester_Register.objects.filter(course=course,semester=semester,status="active"):
                if Student_all.objects.filter(branch=course,previous_pending__gte=1) :
                    obj=Student_all.objects.filter(branch=course,previous_pending__gte=1)
                    for c in obj:
                        p=Student_all.objects.get(id=c.id)
                        enrollment_number=p.enrollment_number
                        if Student_Register.objects.get(enrollment_number=enrollment_number):
                            x=Student_Register.objects.get(enrollment_number=enrollment_number)
                            email=x.email

                            ctx = {
                                'name': c.name,
                                'previous_pending':c.previous_pending,
                                'course': c.branch,
                                'enroll': c.enrollment_number,

                            }
                            message = get_template('faculty_pages/email_tamplate3.html').render(ctx)
                            msg = EmailMessage(
                                'AIT Instiute Fees Submition',
                                message,
                                'Alpine Insitude Of Techonology',
                                [email],

                            )
                            msg.content_subtype = "html"
                            msg.send()


                    else:
                        messages.success(request,"Email Send Successfully ")
                        return render(request, "faculty_pages/check_no_dues.html")

                else:
                    messages.error(request, "error")
                    return render(request, "faculty_pages/check_no_dues.html")



            else:
                messages.error(request, "error")
                return render(request, "faculty_pages/check_no_dues.html")
        else:
            messages.error(request, "error")
            return render(request,"faculty_pages/check_no_dues.html")

    return render(request, "faculty_pages/check_no_dues.html")


def Send_success_email(request):
    faculty_number=request.session['faculty_number']
    obj = Faculty.objects.get(faculty_number=faculty_number)
    faculty_type = obj.faculty_type
    if faculty_type == "HOD":
        if request.method=="POST":
            course=request.POST['course']
            semester=request.POST['semester']
            check=request.POST['check']
            if check=="0":
                if Student_Semester_Register.objects.filter(course=course,semester=semester,status="active"):
                    if Student_all.objects.filter(branch=course,previous_pending=0) :
                        obj=Student_all.objects.filter(branch=course,previous_pending=0)
                        for c in obj:
                            p=Student_all.objects.get(id=c.id)
                            enrollment_number=p.enrollment_number
                            if Student_Register.objects.get(enrollment_number=enrollment_number):
                                x=Student_Register.objects.get(enrollment_number=enrollment_number)
                                email=x.email

                                ctx = {
                                    'name': c.name,
                                    'previous_pending':c.previous_pending,
                                    'course': c.branch,
                                    'enroll': c.enrollment_number,

                                }
                                message = get_template('faculty_pages/email_tamplate4.html').render(ctx)
                                msg = EmailMessage(
                                    'AIT Instiute Fees Submition',
                                    message,
                                    'Alpine Insitude Of Techonology',
                                    [email],

                                )
                                msg.content_subtype = "html"
                                msg.send()


                        else:
                            messages.success(request,"Email Send Successfully ")
                            return render(request, "faculty_pages/check_no_dues.html")

                    else:
                        messages.error(request, "error")
                        return render(request, "faculty_pages/check_no_dues.html")



                else:
                    messages.error(request, "error")
                    return render(request, "faculty_pages/check_no_dues.html")
            else:
                messages.error(request, "error")
                return render(request,"faculty_pages/check_no_dues.html")
    else:
        messages.error(request, "You are not HOD")
        return render(request, "faculty_pages/check_no_dues.html")

    return render(request, "faculty_pages/check_no_dues.html")
