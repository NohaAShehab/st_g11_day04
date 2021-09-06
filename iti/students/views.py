from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# main logic of your app
##
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
def listStudentFun(request,dept):
    instructorname = "Noha"
    # if you want parameter from view to html , You need a dictionary
    # python dictionary
    students = ["Ahmed", "Mohamed", "Ali", "Mostafa"]
    info = {"name": "Noha", "email":"nshehab@iti.gov.eg"}
    context = {"myname": instructorname, "students": students, "dept": dept,
               "info": info}
    return render(request, "students/students.html", context)
