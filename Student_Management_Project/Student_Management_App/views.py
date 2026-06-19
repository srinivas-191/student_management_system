from django.shortcuts import render,redirect
from .models import Students
# Create your views here.
def Home(request):
    students=Students.objects.all()
    return render(request,"home.html",{"students":students})

def Add_student(request):
    if request.method=="POST":
        name=request.POST.get("sname")
        email=request.POST.get("semail")
        course=request.POST.get("scourse")
        age=request.POST.get("sage")
        city=request.POST.get("scity")
        Students.objects.create(
            student_name=name,
            student_email=email,
            course=course,
            student_age=age,
            city=city
        )
        return redirect("home")
    return render(request,"add_student.html")

def Update_student(request,id):
    student=Students.objects.get(id=id)
    print(student)
    if request.method=="POST":
        student.student_name=request.POST.get("sname")
        student.student_email=request.POST.get("semail")
        student.course=request.POST.get("scourse")
        student.student_age=request.POST.get("sage")
        student.city=request.POST.get("scity")
        student.save()
        return redirect("home")
    return render(request,"update_student.html",{"student":student})
def Delete_student(request,id):
    student=Students.objects.get(id=id)
    student.delete()
    return redirect("home")