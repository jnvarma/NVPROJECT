from django.shortcuts import render,redirect
from .models import PythonApplication,JavaApplication,AssApplication,CoordinatorApplication,JavafullApplication,PythonfullApplication
# Create your views here.
def welcome (request):
    return render(request, "welcome.html")
    


def career (request):
    return render(request, "career.html")

def jobs (request):
    return render(request, "jobs.html")

def about (request):
    return render(request, "about.html")

def contact (request):
    return render(request, "contact.html")

def logout (request):
    return redirect (request,"welcome")

def python_application (request):
    if request.method == 'POST':
        # Process form submission
        application = PythonApplication(
            first_name=request.POST['name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            education_type=request.POST['education_type'],
            year_started=request.POST['year_started'],
            year_passed=request.POST['year_passed'],
            skills=request.POST['skills'],
            resume=request.FILES['resume'],
            cover_letter=request.POST['cover-letter']
        )
        application.save()
        return redirect("success_page") 
    return render (request,"python_application.html")

def java_application (request):
    if request.method == 'POST':
        # Process form submission
        application = JavaApplication(
            first_name=request.POST['name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            education_type=request.POST['education_type'],
            year_started=request.POST['year_started'],
            year_passed=request.POST['year_passed'],
            skills=request.POST['skills'],
            resume=request.FILES['resume'],
            cover_letter=request.POST['cover-letter']
        )
        application.save()
        return redirect("success_page")
    return render (request,"java_application.html")

def ass_application (request):
    if request.method == 'POST':
        # Process form submission
        application = AssApplication(
            first_name=request.POST['name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            education_type=request.POST['education_type'],
            year_started=request.POST['year_started'],
            year_passed=request.POST['year_passed'],
            skills=request.POST['skills'],
            resume=request.FILES['resume'],
            cover_letter=request.POST['cover-letter']
        )
        application.save()
        return redirect("success_page")
    return render (request,"ass_application.html")

def coordinator_application (request):
    if request.method == 'POST':
        # Process form submission
        application = CoordinatorApplication(
            first_name=request.POST['name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            education_type=request.POST['education_type'],
            year_started=request.POST['year_started'],
            year_passed=request.POST['year_passed'],
            skills=request.POST['skills'],
            resume=request.FILES['resume'],
            cover_letter=request.POST['cover-letter']
        )
        application.save()
        return redirect("success_page")
    return render (request,"coordinator_application.html")

def java_full_application (request):
    if request.method == 'POST':
        # Process form submission
        application = JavafullApplication(
            first_name=request.POST['name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            education_type=request.POST['education_type'],
            year_started=request.POST['year_started'],
            year_passed=request.POST['year_passed'],
            skills=request.POST['skills'],
            resume=request.FILES['resume'],
            cover_letter=request.POST['cover-letter']
        )
        application.save()
        return redirect("success_page")
    return render (request,"java_full_application.html")

def python_full_application (request):
    if request.method == 'POST':
        # Process form submission
        application = PythonfullApplication(
            first_name=request.POST['name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            education_type=request.POST['education_type'],
            year_started=request.POST['year_started'],
            year_passed=request.POST['year_passed'],
            skills=request.POST['skills'],
            resume=request.FILES['resume'],
            cover_letter=request.POST['cover-letter']
        )
        application.save()
        return redirect("success_page")
    return render (request,"python_full_application.html")
 
def success_page (request):
    return render (request, "success.html")