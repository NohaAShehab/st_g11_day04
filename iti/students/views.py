from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from students.models import Student
from depts.models import Department
from students.forms import StudentForm
from students.forms import StudentModelForm

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
    return render(request, "students/studentprofile.html", context)
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
        students = Student.objects.filter(name__startswith=searchname)
        print(students)
        context = {"searchres": students}
        return render(request, 'students/search.html', context)
    elif request.method == "GET":
        return render(request, 'students/search.html')


def addStudent(request):
    # form = StudentForm()
    form = StudentModelForm()
    # use from the created in forms in py
    if request.method == "GET":
        # departments = Department.objects.all()
        # context = {"depts": departments}
        context = {"form": form}
        return render(request, 'students/addstudent.html', context)

    if request.method == "POST":
        # form = StudentForm(request.POST)
        # if form.is_valid():  # check if the inputs vaidate the model
        #     # create student object
        #     print(request.POST["dept"])
        #     # std = Student()
        #     # std.name = request.POST["name"]
        #     # std.email = request.POST["email"]
        #     # std.img = request.POST["img"]
        #     # std.gender = request.POST["gender"]
        #     # # dept is missing , I need deptartment object
        #     mydept = Department.objects.get(pk=request.POST["dept"])
        #     # std.dept = mydept
        #     # # save it to the database
        #     # std.save()
        #
        #     Student.objects.create(name=request.POST["name"],
        #                        email=request.POST["email"],
        #                        img=request.POST["img"],
        #                        gender=request.POST["gender"],
        #                        dept=mydept)
        #     # return to the all students page
        form = StudentModelForm(request.POST)
        form.save()

        return redirect("allstudents")


def deleteStudent(request, std_id):
    student = get_object_or_404(Student, pk=std_id)
    student.delete()
    # return HttpResponse(student)
    return redirect("allstudents")


def editStudent(request, std_id):
    student = get_object_or_404(Student, pk=std_id)
    if request.method =="GET":
        departments = Department.objects.all()
        if student.gender =="m":
            student.g = True
        elif student.gender =="f":
            student.g = False

        context={"student": student, "depts": departments}
        return render(request, "students/editstudent.html", context)
    if request.method =='POST':
        # student.name = request.POST["name"]
        # student.email = request.POST["email"]
        # student.gender = request.POST["gender"]
        # student.img = request.POST["img"]
        # ## request.POST["dept"]
        mydept = Department.objects.get(pk=request.POST["dept"])
        # student.dept = mydept
        # student.save()

        Student.objects.filter(pk=std_id).update(
            name=request.POST["name"],
            email=request.POST["email"],
            img=request.POST["img"],
            gender=request.POST["gender"],
            dept=mydept)

        return redirect("allstudents")


def updateStudent(request, std_id):
    if request.method == "POST":
        student = get_object_or_404(Student, pk=std_id)
        student.name = request.POST["name"]
        student.email = request.POST["email"]
        student.gender = request.POST["gender"]
        student.img = request.POST["img"]
        ## request.POST["dept"]
        mydept = Department.objects.get(pk=request.POST["dept"])
        student.dept = mydept
        student.save()
        return redirect("allstudents")

