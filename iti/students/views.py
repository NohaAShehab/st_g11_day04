from django.shortcuts import render
from django.http import HttpResponse


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

    # students name, imge   # list of dictionaies
    # students = [
    #     {"name": "Ahmed", "img": "im1.jpg"},
    #     {"name": "Mohamed", "img": "im7.jpg"},
    #     {"name": "Ali", "img": "im3.jpg"},
    #     {"name": "Mostafa", "img": "im5.jpg"},
    #     {"name": "Noha", "img": "im2.jpg"},
    #     {"name": "Radwa", "img": "img.jpg"}
    # ]
    info = {"name": "Noha", "email": "nshehab@iti.gov.eg"}
    context = {"myname": instructorname, "students": students,
               "info": info}
    return render(request, "students/students.html", context)


def studentProfile(request, std_name):
    student = {}
    for std in students:
        if std["name"] == std_name:
            student = std

    context = {"student": student}
    # return HttpResponse(std_name)
    return render(request, "students/studentprofile.html",context)


def aboutus(request):
    return render(request, "students/aboutus.html")


def teststyle(request):
    return render(request, "students/index.html")
