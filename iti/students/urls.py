from django.urls import path
from students.views import home, hello, helloPage, google, \
    listStudentFun, aboutus, teststyle,studentProfile

urlpatterns = [

    # url parameter
    path('home/', home, name="studentshome"),
    path('hello/<myname>/<email>', hello),
    path('hellopage', helloPage),
    path('studentgoogle', google, name="mygoogle"),
    path('liststudents', listStudentFun, name="allstudents"),
    path('aboutus', aboutus, name='aboutus'),
    path('style', teststyle, name='teststyle'),
    path("liststudents/<std_name>", studentProfile, name="studentprofile")

    # courses

]
