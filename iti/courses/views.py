from django.shortcuts import render
from django.http import HttpResponse
from courses.forms import CourseModelForm

# Create your views here.

def testcourses(request):
    # return HttpResponse("this course page")
    return render(request, "courses/courseshome.html")


def addCourse(request):
    # form to add course
    form = CourseModelForm()
    if request.method == "GET":
        context = {"form":form}

        return render(request, "courses/add.html",context)
    elif request.method == "POST":
        form = CourseModelForm(request.POST)
        form.save()

        return HttpResponse("added")

