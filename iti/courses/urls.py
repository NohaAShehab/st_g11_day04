
from django.urls import path
# from students.views import home,hello,helloPage,google,listStudentFun
from courses.views import testcourses
urlpatterns = [

    # you need define the urls file of component student
    # courses
    path('', testcourses)
]
