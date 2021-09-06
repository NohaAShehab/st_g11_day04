from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def testcourses(request):
    # return HttpResponse("this course page")
    return render(request, "courses/courseshome.html")
