from django.urls import path
from students.views import home,hello,helloPage,google,listStudentFun

urlpatterns = [

    # url parameter
    path('home/', home),
    path('hello/<myname>/<email>', hello),
    path('hellopage',helloPage),
    path('mygoogle', google),
    path('liststudent/<dept>', listStudentFun),
    # courses

]
