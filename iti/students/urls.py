from django.urls import path
from students.views import home, hello, helloPage, google, \
    listStudentFun, aboutus, teststyle,studentProfile,search, addStudent, \
    deleteStudent, editStudent, updateStudent


urlpatterns = [

    # url parameter
    path('home/', home, name="studentshome"),
    path('hello/<str:myname>/<email>', hello),
    path('hellopage', helloPage),
    path('studentgoogle', google, name="mygoogle"),
    path('liststudents', listStudentFun, name="allstudents"),
    path('aboutus', aboutus, name='aboutus'),
    path('style', teststyle, name='teststyle'),
    # enforce the request will be sent to the view if only the std_id int
    path("liststudents/<int:std_id>", studentProfile, name="studentprofile"),
    path("searchstudent", search, name="searchstudent"),
    path("add", addStudent, name="addstudent"),
    path("delete/<int:std_id>", deleteStudent, name="deletestudent"),
    path("edit/<int:std_id>", editStudent, name="editstudent"),
    path("update/<int:std_id>", updateStudent, name="updatestudent")


    # courses

]
