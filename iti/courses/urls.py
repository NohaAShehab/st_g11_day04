
from django.urls import path
from . import views

# from students.views import home,hello,helloPage,google,listStudentFun
from courses.views import testcourses, addCourse
urlpatterns = [

    # courses
    # path('', testcourses),
    path('add', addCourse, name="addcourse"),
]
