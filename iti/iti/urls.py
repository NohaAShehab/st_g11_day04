"""iti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from students.views import home,hello,helloPage,google,listStudentFun
from courses.views import testcourses
urlpatterns = [
    path('admin/', admin.site.urls),
    # url parameter
    # path('students/home/', home),
    # path('students/hello/<myname>/<email>', hello),
    # path('students/hellopage',helloPage),
    # path('students/mygoogle', google),
    # path('students/liststudent/<dept>', listStudentFun),
    path("students/", include("students.urls")),
    # you need define the urls file of component student
    # courses
    # path('courses', testcourses)
    path("courses/", include("courses.urls"))
]
