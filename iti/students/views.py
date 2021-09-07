from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from students.models import Student
from depts.models import Department


# Create your views here.

# main logic of your app
##

students = [
    {"name": "Ahmed", "img": "im1.jpg"},
    {"name": "Mohamed", "img": "im7.jpg"},
    {"name": "Ali", "img": "im3.jpg"},
    {"name": "Mostafa", "img": "im5.jpg"},
    {"name": "Noha", "img": "im2.jpg"},
    {"name": "Radwa", "img": "img.jpg"}
]


def home(request):
    # return with httpresponse
    return HttpResponse("<h1> <center> "
                        "<font color ='blue'>Hello World from django </font> <center> <h1>")


def hello(request, myname, email):
    print("abc", myname)
    return HttpResponse(f"<h1> <center> "
                        f"<font color ='blue'>Hello {myname} {email}  </font> <center> <h1>")
    # if myname == 'noha':
    #
    #     return HttpResponse(f"<h1> <center> "
    #                     f"<font color ='blue'>Hello {myname}  </font> <center> <h1>")
    #
    # else:
    #     return HttpResponse(f"<h1> <center> "
    #                         f"<font color ='red'>{myname}  </font> <center> <h1>")


def helloPage(request):
    # return HttpResponse("My hello page")
    return render(request, "students/hello.html")


def google(request):
    return render(request, "students/google.html")


# send parameters from view to html
def listStudentFun(request):
    instructorname = "Noha"
    # if you want parameter from view to html , You need a dictionary
    # python dictionary
    # I need to query the students from the database
    # get students ---> using Model
    # select * from student;
    studentsObjects = Student.objects.all()  # <class 'django.db.models.query.QuerySet'>
    # print(type(studentsObjects)) ## as ---> index
    # return HttpResponse(studentsObjects[0].email)

    info = {"name": "Noha", "email": "nshehab@iti.gov.eg"}
    context = {"myname": instructorname, "students": studentsObjects,
               "info": info}
    return render(request, "students/students.html", context)


def studentProfile(request, std_id):


    # return HttpResponse(std_id)
    # student = Student.objects.get(pk=std_id)
    student = get_object_or_404(Student, pk=std_id)
    # return HttpResponse(student.email)
    print(student.gender)
    if student.gender == 'm':
        student.gender = "Male"
    else:
        student.gender = "Female"

    context = {"student": student}
    # # return HttpResponse(std_name)
    return render(request, "students/studentprofile.html",context)
    # return


def aboutus(request):
    return render(request, "students/aboutus.html")


def teststyle(request):
    return render(request, "students/index.html")


def search(request):
    print(request.method)

    if request.method == "POST":
        print(request.POST["searchname"])
        searchname = request.POST["searchname"]
        ## goto database search about students , with name ali
        students = Student.objects.filter(name=searchname)
        print(students)
        context = {"searchres":students}
        return render(request, 'students/search.html', context)
    elif request.method == "GET":
        return render(request, 'students/search.html')



def addStudent(request):
    if request.method == "GET":
        departments = Department.objects.all()
        context = {"depts": departments}
        return render(request,'students/addstudent.html', context)

    if request.method =="POST":
        # create student object
        print(request.POST["dept"])
        std = Student()
        std.name = request.POST["name"]
        std.email = request.POST["email"]
        std.img = request.POST["img"]
        std.gender = request.POST["gender"]
        # dept is missing , I need deptartment object
        mydept = Department.objects.get(pk=request.POST["dept"])
        std.dept = mydept
        # save it to the database
        std.save()
        # return to the all students page
        return redirect("allstudents")


