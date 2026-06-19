from django.shortcuts import render,redirect
from .models import Students
import re
# Create your views here.
def Home(request):
    students=Students.objects.all()
    return render(request,"home.html",{"students":students})

def Add_student(request):
    errors={}
    if request.method=="POST":
        name=request.POST.get("sname")
        email=request.POST.get("semail")
        course=request.POST.get("scourse")
        age=request.POST.get("sage")
        city=request.POST.get("scity")
        phone=request.POST.get("sphone")
        if not name:
            errors["name"]="name is required"
        
        if email:
            if not re.match(r'^[A-Za-z0-9_%+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}$',email):
                errors["email"]="Enter a valid email address"

            elif Students.objects.filter(student_email=email).exists():
                errors["email"]="Email already exists"
        
        try:
            age=int(age)
            if age<=2 or age>30:
                errors["age"]="Age must between 2 and 30"
        except:
            errors["age"]="age must be a number"

        if not re.fullmatch(r'^[0-9]{10}$',phone):
            errors["phone"]="Enter a valid phone number"
        if not errors:
            Students.objects.create(
                student_name=name,
                student_email=email,
                course=course,
                student_age=age,
                city=city,
                phone=phone
            )
            return redirect("home")
    return render(request,"add_student.html",{"form_data":request.POST,"errors":errors})

def Update_student(request,id):
    errors={}
    student=Students.objects.get(id=id)
    if request.method=="POST":
        student.student_name=request.POST.get("sname")
        student.student_email=request.POST.get("semail")
        student.course=request.POST.get("scourse")
        student.student_age=request.POST.get("sage")
        student.city=request.POST.get("scity")
        student.phone=request.POST.get("sphone")
        if not student.student_name:
            errors["name"]="name is required"
        
        if student.student_email:
            if not re.match(r'^[A-Za-z0-9_%+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}$',student.student_email):
                errors["email"]="Enter a valid email address"

            elif Students.objects.filter(student_email=student.student_email).exclude(id=student.id).exists():
                errors["email"]="Email already exists"
        
        try:
            age=int(student.student_age)
            if age<=2 or age>30:
                errors["age"]="Age must between 2 and 30"
        except:
            errors["age"]="age must be a number"

        if not re.fullmatch(r'^[0-9]{10}$',student.phone):
            errors["phone"]="Enter a valid phone number"
        if not errors:
            student.save()
            return redirect("home")
    return render(request,"update_student.html",{"student":student,"errors":errors})
def Delete_student(request,id):
    student=Students.objects.get(id=id)
    student.delete()
    return redirect("home")